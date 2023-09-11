import logging
import boto3
from botocore.exceptions import ClientError
import os

'''
# AWS S3 configuration
S3_BUCKET = 'your-s3-bucket-name'
S3_ACCESS_KEY = 'your-access-key'
S3_SECRET_KEY = 'your-secret-key'
S3_REGION = 'your-s3-region'

# Initialize an S3 client
s3 = boto3.client('s3', aws_access_key_id=S3_ACCESS_KEY, aws_secret_access_key=S3_SECRET_KEY, region_name=S3_REGION)

'''

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return None
    print(response)
    return response