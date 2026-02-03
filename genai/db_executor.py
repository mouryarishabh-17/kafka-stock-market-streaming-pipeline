import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def run_query(sql: str):
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST", "127.0.0.1"),
        port=os.getenv("POSTGRES_PORT", "5432")
    )

    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows
