from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from script import some_script


default_args = {
    'owners': 'airflow',
    'start_date': datetime.today() - timedelta(days=1)
}

with DAG('pokemon_dag', start_date=datetime(2022, 1, 1),
         schedule_interval='@once',
         catchup=False,
         default_args=default_args) as dag:
    task = PythonOperator(
        task_id='pokemon_script',
        python_callable=some_script,
        dag=dag
    )

#docker-compose up airflow-init
#docker build . --tag extending_airflow:latest 
#docker compose up -d --no-deps --build airflow-webserver airflow-scheduler
#http://localhost:8080
#docker-compose down -v