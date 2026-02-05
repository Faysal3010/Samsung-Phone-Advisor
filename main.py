import re
from ollama import Client
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from db_setup import fetch_all_phones, fetch_phone_by_model
from scraper import seed_database

load_dotenv()

try:
    print("Initializing Database and Seeding Data...")
    seed_database()
    print("Database ready!")
except Exception as e:
    print(f"Database setup failed: {e}")

client = Client()
OLLAMA_MODEL = "deepseek-v3.1:671b-cloud"  # Make sure to run 'ollama pull deepseek-v3.1:671b-cloud'

# 2. Initialize App
app = FastAPI(title="Samsung Advisor")

# 3. Pydantic Models
class UserQuery(BaseModel):
    question: str

class AdviceResponse(BaseModel):
    phone_model: str
    specs: dict
    review: str

# 4. Helper: Extract Model Names using Regex (Agent 1 Logic)
def extract_model_names(question: str) -> List[str]:
    # Patterns to catch common names
    patterns = [
        r'Galaxy\s+S\d+(?:\s+Ultra|\s+Plus)?', 
        r'Galaxy\s+Z\s+(?:Fold|Flip)\s+\d+', 
        r'Galaxy\s+A\d+', 
        r'S\d+\s+Ultra',
        r'S\d+\s+Plus',
        r'S\d+'
    ]
    candidates = []
    for pattern in patterns:
        matches = re.findall(pattern, question, re.IGNORECASE)
        candidates.extend(matches)
    
    # Deduplicate and keep longest matches (e.g. keep "S23 Ultra" over "S23")
    unique_candidates = list(set(candidates))
    unique_candidates.sort(key=len, reverse=True)
    
    final_models = []
    for cand in unique_candidates:
        if not any(cand in existing for existing in final_models):
            final_models.append(cand)
            
    return final_models

# 5. Helper: Generate AI Review (Agent 2 Logic)
def generate_ai_review(specs_list: List[dict], user_question: str) -> str:
    context = ""
    for specs in specs_list:
        context += f"""
    --- Phone: {specs['model_name']} ---
    Release Date: {specs['release_date']}
    Display: {specs['display']}
    Battery: {specs['battery']}
    Camera: {specs['camera']}
    RAM: {specs['ram']}
    Storage: {specs['storage']}
    Price: {specs['price']}
    """
    
    prompt = f"""
    You are a helpful phone assistant. 
    User Question: "{user_question}"
    
    Tech Specs:
    {context}
    
    Task: Write a short, friendly, funny, natural, and helpful answer (max 5 sentences) based on the specs. If multiple phones are listed, compare them.
    """
    
    try:
        response = client.chat(model=OLLAMA_MODEL, messages=[
            {'role': 'user', 'content': prompt}
        ])
        return response['message']['content'].strip()
    except Exception as e:
        return f"I found the specs, but I couldn't generate a review due to a network issue.{e}"


@app.get("/", tags=["Samsung Advisor API is running"])
def home():
    return {"status": "Active", "message": "Samsung Advisor API is running"}

# Route 1: Get list of all phones
@app.get("/phones", tags=["Database"])
def get_all_phones():
    phones = fetch_all_phones()
    return {"count": len(phones), "phones": phones}


# Route 2: Ask the AI Assistant
@app.post("/ask", response_model=AdviceResponse, tags=["AI Agent"])
async def ask_question(query: UserQuery):
    # Step 1: Identify Model
    model_names = extract_model_names(query.question)
    
    if not model_names:
        raise HTTPException(status_code=400, detail="Please mention a specific Samsung model (e.g., S24 Ultra).")
    
    # Step 2: Retrieve Data
    specs_list = []
    for name in model_names:
        data = fetch_phone_by_model(name)
        if data:
            specs_list.append(data)
    
    if not specs_list:
        raise HTTPException(status_code=404, detail=f"Details for '{model_names}' not found in database.")
    
    # Step 3: Generate Review
    review = generate_ai_review(specs_list, query.question)
    
    return AdviceResponse(
        phone_model=", ".join([s['model_name'] for s in specs_list]),
        specs=specs_list[0], # Return first phone specs to satisfy schema
        review=review
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app',reload=True, host= '0.0.0.0',port=8000)