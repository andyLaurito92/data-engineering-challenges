import boto3
from datetime import date

def get_file_names(s3_response):
    filenames = []
    for item in s3_response['Contents']:
        filenames.append(item["Key"])
    return filenames

# s3 = boto3.resource('s3')
# my_bucket = s3.Bucket("sources-medical-publications", endpoint_url="http://localhost:4566", use_ssl=False)
# s
my_bucket = "sources-medical-publications"
s3_endpoint = "http://localhost:4566"
s3_client = boto3.client("s3", endpoint_url=s3_endpoint, use_ssl=False)

target_filename = 'allfiles.gz'
today = date.today().strftime("%y/%m/%d")
bucket_result = "output-medical-publications"

bufferSize = 8  # Adjust this according to how "memory efficient" you need the program to be.

with open(target_filename, 'wb') as destFile:
    for fileName in get_file_names(s3_client.list_objects(Bucket=my_bucket)):
        with urlopen(Request(s3_endpoint + "/" + my_bucket + "/" + fileName, headers={"Accept-Encoding": "gzip"})) as response, \
     GzipFile(fileobj=response) as gzipfile:
            destFile.write(gzipfile.read())

            
s3_client = boto3.client("s3", endpoint_url="http://localhost:4566", use_ssl=False)
try:
    response = s3_client.upload_file(target_filename, bucket_result, today+"/"+target_filename)
except ClientError as e:
    logging.error(e)




