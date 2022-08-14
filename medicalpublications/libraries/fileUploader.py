import logging
import boto3
from botocore.exceptions import ClientError

class S3FileUploader:
    s3_endpoint = "http://localhost:4566"

    @classmethod
    def get_client(cls):
        return boto3.client("s3", endpoint_url=cls.s3_endpoint, use_ssl=False)

    @classmethod
    def upload_bytes(cls, my_key, my_content, my_bucket):
        ## TODO: Add check that validates that size is always under lambda maximum
        s3_client = S3FileUploader.get_client()
        try:
            response = s3_client.put_object(Body=my_content, Bucket=my_bucket, Key=my_key)
        except ClientError as e:
            logging.error(e)

    @classmethod
    def upload_file(cls, key, filename, bucket):
        s3_client = cls.get_client()
        try:
            response = s3_client.upload_file(filename, bucket, key)
        except ClientError as e:
            print(e)
            logging.error(e)

    @classmethod
    def get_files(cls, bucket):
        print(bucket)
        s3_client = cls.get_client()
        s3_response = s3_client.list_objects(Bucket=bucket)

        filenames = []
        for item in s3_response['Contents']:
            filenames.append(item["Key"])
        return filenames
