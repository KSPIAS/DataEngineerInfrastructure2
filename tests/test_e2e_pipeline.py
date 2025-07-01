import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_USER= os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD= os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB= os.getenv("POSTGRES_DB")
POSTGRES_SCHEMA= os.getenv("POSTGRES_SCHEMA")

def test_pipeline_inserted_data():
    conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        # host=POSTGRES_HOST,
        host=127.0.0.1 #Git Actions
        port=POSTGRES_PORT
    )
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {POSTGRES_SCHEMA}.weather;")
    count = cur.fetchone()[0]
    assert count > 0
    conn.close()
