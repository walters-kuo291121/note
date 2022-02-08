import logging
import boto3
from botocore.exceptions import ClientError
import os


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
        return False
    return True
'''
#https://s3-ap-northeast-1.amazonaws.com/dev-env-bicket/avatar.jpg
images.awsexamplebucket1.net.s3.us-west-2.amazonaws.com
                             s3.ap-northeast-1.amazonaws.com

https://img-dev.topyl666.com.s3.Region.amazonaws.com/key-name
https://img-dev.topyl666.com.s3.ap-northeast-1.amazonaws.com/hello.jpg
https://img-dev.topyl666.com/hello.jpg'''
BUCKET_NAME = "img-dev.topyl666.com"
FILE_NAME = "hello.jpg"
s3_client = boto3.client('s3')

try:
    response = s3_client.upload_file(FILE_NAME, BUCKET_NAME, f'{FILE_NAME}', ExtraArgs={'ACL': 'public-read'})
    #response = s3_client.upload_file(FILE_NAME, BUCKET_NAME, f'test/{FILE_NAME}')
except ClientError as e:
    logging.error(e)
exit()

s3_resource = boto3.resource('s3')
s3.delete_object(Bucket=BUCKET_NAME, Key=FILE_NAME)

s3_resource.meta.client.upload_file(
    f'./{FILE_NAME}',
    BUCKET_NAME,
    FILE_NAME,
    ExtraArgs={'ACL': 'public-read'})

'''s3.upload_file(
    'FILE_NAME', 'BUCKET_NAME', 'OBJECT_NAME',
    ExtraArgs={'ACL': 'public-read'}
)

location = boto3.client('s3').get_bucket_location(Bucket=BUCKET_NAME)['LocationConstraint']





#boto3.resource('s3').ObjectAcl(BUCKET_NAME, FILE_NAME).put(ACL='public-read')
s3 = boto3.resource('s3')
object_acl = s3.ObjectAcl(BUCKET_NAME, FILE_NAME)
#print(object_acl.grants)
#exit()

#response = object_acl.put(ACL='public-read')
response = client.put_bucket_policy(Bucket=BUCKET_NAME, Policy='public-read')

url = f"https://s3-{location}.amazonaws.com/{BUCKET_NAME}/{FILE_NAME}"
print(url)

'''