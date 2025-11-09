import boto3

bucket_name='todaysdatebucket28102025'
client=boto3.client('s3')
response=client.delete_bucket(Bucket=bucket_name)