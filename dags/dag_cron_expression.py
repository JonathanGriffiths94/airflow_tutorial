from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': "JonnyG",
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id="dag_cron_expression_v1",
    default_args=default_args,
    start_date=datetime(2022, 11, 17),
    schedule_interval='40 4 * * *'
) as dag:
    task1 = BashOperator(
        task_id="Task1",
        bash_command="echo Dag with cron expression!"
    )

    task1
