import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT", "5432")
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS phones;")
        cursor.execute("""
            CREATE TABLE phones (
                id SERIAL PRIMARY KEY,
                model_name TEXT UNIQUE,
                release_date TEXT,
                display TEXT,
                battery TEXT,
                camera TEXT,
                ram TEXT,
                storage TEXT,
                price TEXT
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("Database table 'phones' created successfully.")
        
# ... (fetch functions remain the same) ...
def fetch_all_phones():
    conn = get_db_connection()
    if not conn: return []
    cursor = conn.cursor()
    cursor.execute("SELECT model_name, price FROM phones ORDER BY model_name;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"model": row[0], "price": row[1]} for row in rows]

def fetch_phone_by_model(model_name: str):
    conn = get_db_connection()
    if not conn: return None
    cursor = conn.cursor()
    query = """
        SELECT id, model_name, release_date, display, battery, camera, RAM, storage, price
        FROM phones
        WHERE model_name ILIKE %s
        LIMIT 1;
    """
    cursor.execute(query, (f'%{model_name}%',))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if row:
        return {
            'id': row[0], 'model_name': row[1], 'release_date': row[2],
            'display': row[3], 'battery': row[4], 'camera': row[5],
            'ram': row[6], 'storage': row[7], 'price': row[8]
        }
    return None

if __name__ == "__main__":
    get_db_connection()
    create_table()
    fetch_all_phones()
