# Weather Pipeline 🌦️

ETL pipeline สำหรับดึงข้อมูลสภาพอากาศจาก Weatherstack API และโหลดเข้า PostgreSQL ด้วย Docker + Python.

## Features

- Extract → Transform → Load (ETL)
- ใช้ `.env` สำหรับความปลอดภัย
- รัน PostgreSQL ผ่าน Docker
- พร้อมต่อยอด Airflow + Monitoring

## Structure
weather_pipeline/
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── docker-compose.yml
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py


## Getting Started
```bash
docker-compose up -d
python scripts/load.py
