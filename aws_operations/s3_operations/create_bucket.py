from datetime import date
import boto3

#bucket_name='todaysdatebucket'+f'{date.today()}'
bucket_name='aws-sam-cli-managed-default-samclisourcebucket-uz1dt28rddxw'
client=boto3.client('s3')

response=client.create_bucket(Bucket=bucket_name)

print(response)