from aws_connection import s3_resource, s3_client
from flaskr.db_setup import session
from flaskr.models import Bucket

# Methods
def get_files(bucket_name):
    files=[]
    bucket = s3_resource.Bucket(bucket_name)
    for file in bucket.objects.all():
        files.append(file.key)
    return files

def get_bucket_name(user):
    
    bucket = Bucket.query.filter_by(user_id=user.id).first()

    if not bucket:

        str = 'bucket-{0}-shopify-challenge-alex'.format(user.id)
        s3_resource.create_bucket(Bucket=str)
        bucket = Bucket(user.id, str)
        session.add(bucket)
        session.commit()

        
        return str

    return bucket.name