# Task 2: Samsung-Phone-Advisor
An intelligent AI-powered backend system that provides personalized Samsung phone recommendations using local LLMs (Ollama) and FastAPI.

## Features

- **AI-Powered Recommendations**: Uses Ollama (DeepSeek v3.1) to analyze user queries and provide intelligent phone recommendations
- **Phone Database**: PostgreSQL database storing Samsung phone specifications
- **Regular Expression module**: Intelligent extraction of multiple phone model names for comparisons
- **RESTful API**: FastAPI-based backend with clear endpoints for phone queries and recommendations
- **Automatic Setup**: Database tables and sample data are automatically seeded on server startup
- **Environment Management**: Secure configuration using .env files

## Tech Stack

- **Backend Framework**: FastAPI, Uvicorn
- **Database**: PostgreSQL with psycopg2
- **AI**: Ollama (DeepSeek v3.1 cloud)
- **Web Scraping**: BeautifulSoup, Requests
- **Validation**: Pydantic
- **Configuration**: python-dotenv

## Installation
## (1) Clone the repository
   ```bash
   git clone <repository-url>
   cd Samsung-Phone-Advisor
   ```
## (2) Create virtual environment

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```
### Mac/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```
## (3) Install dependencies
```bash
pip install -r requirements.txt
```

Running Cloud models
Ollama’s cloud models require an account on ollama.com. To sign in or create an account, run:

```bash
ollama signin
```
First, pull a cloud model so it can be accessed:

```bash
ollama run deepseek-v3.1:671b-cloud
```
 
---

## Project Structure


```yaml
├── main.py               
├── db_setup.py          
├── scraper.py            
├── requirements.txt     
└── README.md            
```

---


▶️ How to Run into terminal
```cmd

python main.py
```

