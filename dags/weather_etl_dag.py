from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
# Correct import after moving `scripts/` inside `dags/`
from scripts.extract import extract_weather
from scripts.transform import transform_weather
from scripts.load import load_weather

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

#DAG must be assigned to a variable named dag.
with DAG(
    dag_id='weather_data_etl',
    default_args=default_args,
    schedule_interval='@hourly',  # Can change to '@daily'
    catchup=False
) as dag:

    # Define tasks
    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract_weather,
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform_weather,
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load_weather,
    )

    # Task pipeline
    extract_task >> transform_task >> load_task
