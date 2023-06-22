from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


default_args = {
    "owner": "admin",
    "start_date": datetime(2023, 1, 1),
}

with DAG(
    dag_id="first",
    description="My first DAG",
    default_args=default_args,
    schedule_interval="*/10 * * * *", # every 10 minutes
    
) as dag:
    task1 = BashOperator(
        task_id="task1",
        bash_command="echo 'Hello World!'",
    )
    task2 = BashOperator(
        task_id="task2",
        bash_command="sleep 10",
    )
