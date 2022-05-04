from airflow.operators.python import PythonOperator


def get_matplotlib():
    import matplotlib
    print(f"matplotlib with version: {matplotlib.__version__}")


get_matplotlib = PythonOperator(
    task_id='get_matplotlib',
    python_callable=get_matplotlib
)
