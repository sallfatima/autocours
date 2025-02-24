"""
DAG Airflow pour orchestrer la génération des cours et la mise à jour du modèle.
Ce DAG s'exécute quotidiennement.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'autocours',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'autocours_dag',
    default_args=default_args,
    description='DAG pour générer et mettre à jour les cours',
    schedule_interval=timedelta(days=1),
)

generate_course = BashOperator(
    task_id='generate_course_task',
    bash_command='python app/main.py "Exemple de sujet"',
    dag=dag,
)

generate_course
