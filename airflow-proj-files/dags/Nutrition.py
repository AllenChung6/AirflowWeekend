from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.papermill.operators.papermill import PapermillOperator
# pip install "apache-airflow[celery]==2.2.5"

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
        dag_id='example_papermill_operator',
        default_args=default_args,
        schedule_interval='0 0 * * *',
        start_date=datetime(2022, 4, 10),
        template_searchpath='/Users/allenc/PyCharmProjects/AirflowWeekend/airflow-proj-files/',
        catchup=False
) as dag_1:
    notebook_task = PapermillOperator(
        task_id="run_Nutritional_Facts.ipynb",
        input_nb="airflow-proj-files/Nutritional_Facts.ipynb",
        output_nb="airflow-proj-files/out-{{ execution_date }}.ipynb",
        parameters={"execution_date": "{{ execution_date }}"},
    )

