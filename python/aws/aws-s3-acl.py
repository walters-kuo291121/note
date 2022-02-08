import boto3


BUCKET_NAME = "dev-env-bicket"
FILE_NAME = "avatar.jpg"
s3 = boto3.resource('s3')
bucket_acl = s3.BucketAcl(BUCKET_NAME)
print(bucket_acl.grants)