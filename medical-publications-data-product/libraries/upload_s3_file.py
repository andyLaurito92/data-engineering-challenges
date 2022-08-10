import logging
import boto3
from botocore.exceptions import ClientError

class S3FileUploader:
    @classmethod
    def upload_bytes(self, my_key, my_content, my_bucket):
        ## TODO: Add check that validates that size is always under lambda maximum
        s3_client = boto3.client("s3", endpoint_url="http://localhost:4566", use_ssl=False)
        try:
            response = s3_client.put_object(Body=my_content, Bucket=my_bucket, Key=my_key)
        except ClientError as e:
            logging.error(e)


