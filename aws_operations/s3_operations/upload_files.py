import boto3
import os

bucket_name='useforgenralpurpose'
orders_file=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'/codeplace/retails_parquet_datasets/'+'orders.parquet'
products_file=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'/codeplace/retails_parquet_datasets/'+'products.parquet'
reviews_file=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'/codeplace/retails_parquet_datasets/'+'reviews.parquet'
users_file=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'/codeplace/retails_parquet_datasets/'+'users.parquet'
client=boto3.client('s3')
# When you upload an object with a key like myfolder/myfile.txt, S3 automatically creates the myfolder/ prefix if it doesn't already exist
orders_file=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'/codeplace/retails_parquet_datasets/'+'orders.parquet'
client.upload_file(orders_file,bucket_name,'parquet/orders.parquet')
client.upload_file(products_file,bucket_name,'parquet/products.parquet')
client.upload_file(reviews_file,bucket_name,'parquet/reviews.parquet')
client.upload_file(users_file,bucket_name,'parquet/users.parquet')