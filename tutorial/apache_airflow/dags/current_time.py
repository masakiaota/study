from datetime import datetime, timedelta
from pathlib import Path

savepath = Path('/opt/airflow/logs/output')
if not savepath.exists():
    savepath.mkdir()

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'masaki',
    'depends_on_past': False,
    'email': ['aotamasakimail@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}


dag = DAG(
    'make_current_time_files',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(minutes=1),
    # schedule_interval='* * * * *', #これでも1分ごとになるはずなんだけどなぁ
    start_date=datetime.now() - timedelta(seconds=30),
    # start_date=days_ago(0),
    tags=['example'],
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)

# subt1 = BashOperator(
#     task_id='mkdir_tmp',
#     bash_command='mkdir /tmp/working',
#     dag=dag
# )


t2 = BashOperator(
    task_id='touch_datetxt',
    bash_command=f'touch {savepath.as_posix()}/$(date +"%Y年%m月%d日%H時%M分%S秒").txt',
    dag=dag)

t3 = BashOperator(
    task_id='show_all_files',
    bash_command=f'ls {savepath.as_posix()}',
    dag=dag)


t1 >> t2 >> t3
