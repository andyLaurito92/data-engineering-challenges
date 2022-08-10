import gzip
from urllib.request import urlopen, Request
import boto3
from botocore.exceptions import ClientError


s3_endpoint = "http://localhost:4566/sources-medical-publications/"
date = "2021/12/13/"
example_file = "pubmed22n1115.xml.gz"
url = s3_endpoint + date + example_file

uncompress_file = "pubmed22n1115.xml"
bucket_name = "uncompressed-medical-publications"

from gzip import GzipFile
from urllib.request import urlopen, Request

with urlopen(Request(url, headers={"Accept-Encoding": "gzip"})) as response, \
     GzipFile(fileobj=response) as gzipfile:
    content = gzipfile.read()
    s3_client = boto3.client("s3", endpoint_url="http://localhost:4566", use_ssl=False)
    try:
        #response = s3_client.upload_file(xml_file, bucket_name, date+uncompress_file)
        response = s3_client.put_object(Body=content, Bucket=bucket_name, Key=date+uncompress_file)

    except ClientError as e:
       logging.error(e)
