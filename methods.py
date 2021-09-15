from aws_connection import s3_resource
from config import *

# Methods
def get_files():
    files=[]
    bucket = s3_resource.Bucket(BUCKET_NAME)
    for file in bucket.objects.all():
        files.append(file.key)
    return files