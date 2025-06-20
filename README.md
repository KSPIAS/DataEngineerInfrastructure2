# Weather Pipeline 🌦️

ETL pipeline สำหรับดึงข้อมูลสภาพอากาศจาก Weatherstack API
และโหลดเข้า PostgreSQL ด้วย Docker + Python + Airflow + GCP Cloud SQL PostgreSQL + Terraform.

## Features
- Extract → Transform → Load (ETL)
- ใช้ `.env` สำหรับความปลอดภัย
- รัน PostgreSQL ผ่าน Docker
- Schedule Airflow
- Deploy ไปบน GCP
- Use Terraform

## Structure
```plaintext
weather_pipeline/
├── airflow/                       🔹 Config และ DAGs
│   ├── dags/
│   │   └── weather_dag.py         ✅ DAG schedule ETL
infra/
│   ├── creds.json
│   ├── main.tf
│   ├── providers.tf
│   ├── terraform.tfvars
│   ├── variables.tf
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── sql/
│   └── init_schema.sql            ✅ สร้าง schema ETL + airflow
├── .env
├── .env.example
├── .gitignore
├── docker-compose.yml             ✅ รัน PostgreSQL + Airflow
├── README.md
├── requirements.txt
```

## Getting Started
```bash
docker-compose up -d
python scripts/load.py

docker-compose down -v  # ลบ container + volume (ต้องใช้ -v)
docker-compose up -d    # รันใหม่ จะสร้าง schema ให้อัตโนมัติ

http://localhost:8080 #Airflow
http://localhost:3000 #Grafana
```
