from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime , timedelta


default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='our_first_dag',
    default_args = default_args,
    description='This is our first dag that we write',
    start_date = datetime(2022,7,21,2),
    schedule_interval = '@daily',
) as dag: 
    task1 = BashOperator(
        task_id = 'task1',
        bash_command = "echo  hello world, first task",

    )
    task2 = BashOperator(
        task_id = 'task2',
        bash_command = "echo , second task",
    )
    task3 = BashOperator(
        task_id = 'task3',
        bash_command = "echo , third task",
    )
    task1 >> task2 # task1.set_downstream(task2)
    task1 >> task3 # task2.set_downstream(task3)
    # task1 