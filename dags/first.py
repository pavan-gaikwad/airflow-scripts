from airflow import DAG
from airflow.operators.bash_operator import BashOperator


default_args = {
    "owner": "admin"
}

with DAG(
    dag_id="first",
    description="My first DAG",
) as dag:
    task1 = BashOperator(
        task_id="task1",
        bash_command="echo 'Hello World!'"
    )
