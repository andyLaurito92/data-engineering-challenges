import requests
import logging
import boto3
from botocore.exceptions import ClientError
import os


base_url = "https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/"
example_file = "pubmed22n1115.xml.gz"
date = "2021/12/13/"
bucket_name = "sources-medical-publications"

## TODO: Add check that validates that size is always under lambda maximum
result = requests.get(base_url + example_file)

s3_client = boto3.client("s3", endpoint_url="http://localhost:4566", use_ssl=False)
try:
    response = s3_client.put_object(Body=result.content, Bucket=bucket_name, Key=date+example_file)
except ClientError as e:
    logging.error(e)
