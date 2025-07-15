from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'elt_pipeline_dag',
    default_args=default_args,
    description='Run the ELT pipeline hourly',
    schedule_interval='0 * * * *',  # Every hour
    start_date=datetime(2024, 1, 1),
    catchup=False,
)

run_pipeline = BashOperator(
    task_id='run_elt_pipeline',
    bash_command='cd /opt/elt_pipeline && python pipeline.py',
    dag=dag,
)
