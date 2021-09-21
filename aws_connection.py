import boto3

# Create connection to s3 bucket
s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')