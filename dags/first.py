from airflow import DAG

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
