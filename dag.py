from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from extract import getnews

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 4, 13),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}
with DAG(
    'news_extraction_dag',
    default_args=default_args,
    description='A DAG to extract news articles about Tesla',
    schedule_interval='*/5 * * * *',
    catchup=False,
) as dag:
    
    news_task = PythonOperator(
        task_id='extract_news',
        python_callable=getnews,
        op_kwargs={'query': 'tesla'}
    )
