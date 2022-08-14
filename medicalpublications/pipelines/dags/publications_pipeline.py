from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

from medicalpublications.input.read import read
from medicalpublications.internal.uncompress import unzip 
from medicalpublications.output.createoutput import createUniqueFile

with DAG("medical_publications_pipeline", 
         start_date=datetime(2022, 8 ,14), # start date, the 1st of January 2021 
         schedule_interval='@daily',  # Cron expression, here it is a preset of Airflow, @daily means once every day.
         catchup=False  # Catchup 
         ) as dag:

    extract_files = BashOperator(task_id="Extract_from_ncbi", bash_command="curl -X GET https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/pubmed22n1115.xml.gz --output pubmed22n1115.xml.gz")
    #extract_files = PythonOperator(task_id="Extract_from_ncbi", python_callable=read)
    uncompress_files = PythonOperator(task_id="Uncompress", python_callable=unzip)
    all_in_one = PythonOperator(task_id="create_one_in_all_file", python_callable=createUniqueFile)

    extract_files >> [uncompress_files, all_in_one]
    
