FROM apache/airflow:2.8.1-python3.12
USER root
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
USER airflow
