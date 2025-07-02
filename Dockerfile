FROM apache/airflow:2.8.1-python3.9

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dags/ /opt/airflow/dags/
COPY scripts/ /opt/airflow/scripts/
COPY .env /opt/airflow/.env

ENV AIRFLOW_HOME=/opt/airflow
