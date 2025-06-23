import os
import psycopg2
from dotenv import load_dotenv
from extract import extract_weather
from transform import transform
import logging
logger = logging.getLogger("weather_pipeline")
logger.setLevel(logging.INFO)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.notifier import notify_telegram

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    dbname=os.getenv("POSTGRES_DB")
)

try:
    def ensure_schema_and_table():
        logger.info("🚀 เริ่มกระบวนการตรวจสอบ schema/table")
        with conn.cursor() as cur:
            cur.execute(f"CREATE SCHEMA IF NOT EXISTS {os.getenv('POSTGRES_SCHEMA')}")
            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS {os.getenv('POSTGRES_SCHEMA')}.weather (
                    city TEXT,
                    country TEXT,
                    temperature FLOAT,
                    humidity FLOAT,
                    timestamp TIMESTAMP
                )
            """)
            conn.commit()
        logger.info("✅ ตรวจสอบ schema/table แล้ว")

    def load(data):
        logger.info("🚀 เริ่มกระบวนการโหลดข้อมูล Weather API")
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO {os.getenv('POSTGRES_SCHEMA')}.weather (city, country, temperature, humidity, timestamp)
                VALUES (%s, %s, %s, %s, %s)
            """, (data["city"], data["country"], data["temperature"], data["humidity"], data["timestamp"]))
            conn.commit()
            conn.close()

            # logging.basicConfig(
            #     format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
            #     level=logging.INFO
            # )

            # logger.info("โหลดข้อมูลจาก Weather API สำเร็จ")

        logger.info("✅ โหลดข้อมูลเข้า PostgreSQL เรียบร้อยแล้ว")
        notify_telegram("✅ *Weather ETL Success!* ข้อมูลอัปเดตเรียบร้อยแล้ว ☀️")

except Exception as e:
        logger.exception("❌ เกิดข้อผิดพลาดใน Weather ETL Pipeline")
        notify_telegram(f"❌ *Weather ETL Failed!*\nError: `{e}`")
        raise

if __name__ == "__main__":
    ensure_schema_and_table()
    raw_data = extract_weather()
    clean_data = transform(raw_data)
    load(clean_data)
