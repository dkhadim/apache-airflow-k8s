from datetime import datetime

from airflow import DAG
from airflow.decorators import task

# Adding defaults_args

# Using catchup=False

with DAG(
        dag_id="hello_world",
        start_date=datetime(2024, 5, 23),
        schedule="0 * * * *",
        tags=["hello"]
    ) as dag:
    
    @task()
    def say_hello():
        print("Hello, ")
        
    @task()
    def say_world():
        print("World guys !")
        
    say_hello() >> say_world()