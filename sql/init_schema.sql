-- สร้าง schema สำหรับ ETL
CREATE SCHEMA IF NOT EXISTS api_data;

-- สร้าง schema สำหรับ Airflow (รองรับการใช้ later)
CREATE SCHEMA IF NOT EXISTS airflow;

-- Optional: ตารางใน schema api_data
CREATE TABLE IF NOT EXISTS api_data.weather (
    city TEXT,
    country TEXT,
    temperature FLOAT,
    humidity FLOAT,
    timestamp TIMESTAMP
);
