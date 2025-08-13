import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id="tenant1_dag",
    start_date=datetime.datetime(2025, 8, 13),
    schedule="@daily",
):
    EmptyOperator(task_id="task")