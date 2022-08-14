from datetime import date
from urllib.request import urlopen, Request
from gzip import GzipFile
from medicalpublications.libraries.fileUploader import S3FileUploader

def createUniqueFile():
    my_bucket = "sources-medical-publications"
    s3_endpoint = "http://localhost:4566"

    target_filename = 'allfiles.gz'
    today = date.today().strftime("%y/%m/%d")
    bucket_result = "output-medical-publications"

    bufferSize = 8  # Adjust this according to how "memory efficient" you need the program to be.

    with open("/tmp/" +target_filename, 'wb') as destFile:
        print("heey")
        for fileName in S3FileUploader.get_files(my_bucket):#get_file_names(s3_client.list_objects(Bucket=my_bucket)):
            with urlopen(Request(s3_endpoint + "/" + my_bucket + "/" + fileName, headers={"Accept-Encoding": "gzip"})) as response, \
                 GzipFile(fileobj=response) as gzipfile:
                destFile.write(gzipfile.read())

    S3FileUploader.upload_file(today+"/"+target_filename, "/tmp/" + target_filename, bucket_result)
