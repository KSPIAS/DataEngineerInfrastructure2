FROM apache/airflow:2.8.1-python3.9

ARG AIRFLOW_CONN_DB
ARG AIRFLOW__CORE__EXECUTOR

ENV AIRFLOW_CONN_DB=$AIRFLOW_CONN_DB
ENV AIRFLOW__CORE__EXECUTOR=$AIRFLOW__CORE__EXECUTOR

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dags/ /opt/airflow/dags/
COPY scripts/ /opt/airflow/scripts/

ENV AIRFLOW_HOME=/opt/airflow
