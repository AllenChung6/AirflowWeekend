from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from execute_script import nutrition_script

# pip install "apache-airflow[celery]==2.2.5"

default_args = {
    'owners': 'airflow',
    'start_date': datetime.today() - timedelta(days=1)
}

with DAG('nutrition_dag', start_date=datetime(2022, 1, 1),
         schedule_interval='@once',
         catchup=False,
         default_args=default_args) as dag:

    task = PythonOperator(
        task_id="execute_script",
        python_callable=nutrition_script,
        dag=dag
    )
