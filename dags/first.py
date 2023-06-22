from airflow import DAG
from airflow.operators.bash_operator import BashOperator


default_args = {
    "owner": "admin",
    "start_date": datetime(2023, 1, 1),
}

with DAG(
    dag_id="first",
    description="My first DAG",
    default_args=default_args,
    
) as dag:
    task1 = BashOperator(
        task_id="task1",
        bash_command="echo 'Hello World!'",
    )
