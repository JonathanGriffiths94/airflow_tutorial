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
    start_date=datetime(2022, 11, 1),
    schedule_interval='00 12 * * tue-fri'
) as dag:
    task1 = BashOperator(
        task_id="Task1",
        bash_command="echo Dag with cron expression!"
    )

    task1
