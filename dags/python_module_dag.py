from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'JG13',
    'retries': 5,
    'retry_interval': timedelta(minutes=5)
}


def get_sklearn():
    import sklearn
    print(f'Get scikit-learn version: {sklearn.__version__}')


def get_matplotlib():
    import matplotlib
    print(f'Get matplotlib version: {matplotlib.__version__}')


with DAG(
    dag_id="dag_python_module_v2",
    default_args=default_args,
    start_date=datetime(2022, 11, 22),
    schedule_interval='@daily'
) as dag:

    get_sklearn = PythonOperator(
        task_id='get_sklearn',
        python_callable=get_sklearn
    )

    get_matplotlib = PythonOperator(
        task_id='get_matplotlib',
        python_callable=get_matplotlib
    )

    get_sklearn >> get_matplotlib

