from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# Define default arguments
default_args = {
    "owner": "admin",
    "depends_on_past": False,
    "start_date": datetime(2023, 6, 22),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

for i in range(1, 4):
    dag_id = f"docker_image_build-{str(i)}"
    # Instantiate the DAG
    dag = DAG(dag_id, default_args=default_args, schedule_interval=None)

    # Define the Git repository URL and the Docker image name
    GIT_REPO_URL = "https://github.com/your-username/your-repo.git"
    DOCKER_IMAGE_NAME = "your-docker-hub-username/your-image-name:your-tag"
    bash_script_path = "../scripts/run-automation.sh"

    # Define the tasks
    clone_repo = BashOperator(
        task_id="clone_repo",
        bash_command=f"bash {bash_script_path}",
        dag=dag,
    )

    build_docker_image = BashOperator(
        task_id="build_docker_image",
        bash_command="echo 'cd /tmp/repo/centos7 && docker build -t {} .'".format(DOCKER_IMAGE_NAME),
        dag=dag,
    )

    upload_docker_image = BashOperator(
        task_id="upload_docker_image",
        bash_command="echo 'docker push {}'".format(DOCKER_IMAGE_NAME),
        dag=dag,
    )

    # Define the task dependencies
    clone_repo >> build_docker_image >> upload_docker_image
    globals()[dag_id] = dag