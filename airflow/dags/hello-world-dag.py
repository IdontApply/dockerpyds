from airflow.utils import dates
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
print('hello \n\n\n')
default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': dates.days_ago(2),
    #'email': ['airflow@example.com'],
    #'email_on_failure': False,
    #'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    #'schedule_interval': '@once',
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}
def print_hello():
    return 'hello world!'

dag = DAG('Helloworld', default_args=default_args, schedule_interval='@once')

t1 = BashOperator(
    task_id='task_1',
    bash_command='echo "Hello World from Task 1"',
    dag=dag)

t2 = BashOperator(
    task_id='task_2',
    bash_command='echo "Hello World from Task 2"',
    dag=dag)

t3 = BashOperator(
    task_id='task_3',
    bash_command='echo "Hello World from Task 3"',
    dag=dag)

t4 = BashOperator(
    task_id='task_4',
    bash_command='echo "Hello World from Task 4"',
    dag=dag)
t5 = PythonOperator(
    task_id='task_5',
    python_callable=print_hello,
    dag=dag
)
t2.set_upstream(t1)
t3.set_upstream(t1)
t4.set_upstream(t2)
t4.set_upstream(t3)
t5.set_upstream(t4)


