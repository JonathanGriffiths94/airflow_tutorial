from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"Hello World! My name is {first_name} {last_name}, " 
          f"and i am {age} years old!")


def get_name(ti):
    ti.xcom_push(key='first_name', value='Jonny')
    ti.xcom_push(key='last_name', value='Griffiths')


def get_age(ti):
    ti.xcom_push(key='age', value=28)


with DAG(
    dag_id='first_python_dag_v6',
    description="DAG using python",
    default_args=default_args,
    start_date=datetime(2022, 11, 17, 10),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        #op_kwargs={'age': 28}
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task2, task3] >> task1
