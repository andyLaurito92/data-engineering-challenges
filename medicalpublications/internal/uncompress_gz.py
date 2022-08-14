from gzip import GzipFile
from urllib.request import urlopen, Request
from medicalpublications.libraries.fileUploader import S3FileUploader

s3_endpoint = "http://localhost:4566/sources-medical-publications/"
date = "2021/12/13/"
example_file = "pubmed22n1115.xml.gz"
url = s3_endpoint + date + example_file

uncompress_file = "pubmed22n1115.xml"
bucket_name = "uncompressed-medical-publications"


with urlopen(Request(url, headers={"Accept-Encoding": "gzip"})) as response, \
     GzipFile(fileobj=response) as gzipfile:
    content = gzipfile.read()
    S3FileUploader.upload_bytes(date+uncompress_file, content, bucket_name)
