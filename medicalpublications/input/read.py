import requests
from medicalpublications.libraries.fileUploader import S3FileUploader

def read():
    base_url = "https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/"
    example_file = "pubmed22n1115.xml.gz"
    date = "2021/12/13/"
    bucket_name = "sources-medical-publications"

    ## TODO: Add check that validates that size is always under lambda maximum
    result = requests.get(base_url + example_file)

    S3FileUploader.upload_bytes(date+example_file, result.content, bucket_name)
