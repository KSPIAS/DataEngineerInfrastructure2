from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
# import os

# ปรับ path ให้รัน script ได้
sys.path.append('/opt/airflow/scripts')

from extract import extract_weather
from transform import transform
from load import load, ensure_schema_and_table

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="weather_etl_dag",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="ensure_schema",
        python_callable=ensure_schema_and_table
    )

    t2 = PythonOperator(
        task_id="extract",
        python_callable=extract_weather
    )

    def transform_task(ti):
        raw = ti.xcom_pull(task_ids="extract")
        return transform(raw)

    t3 = PythonOperator(
        task_id="transform",
        python_callable=transform_task
    )

    def load_task(ti):
        data = ti.xcom_pull(task_ids="transform")
        load(data)

    t4 = PythonOperator(
        task_id="load",
        python_callable=load_task
    )

    t1 >> t2 >> t3 >> t4
