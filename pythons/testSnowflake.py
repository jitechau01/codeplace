from snowflake_conn import cur
    
cur.execute("""use role accountadmin""")
cur.execute("""use warehouse compute_wh""")
#create s3 integration object
def create_SNF_AWS_S3_INT():
    cur.execute("""create storage integration s3_integration
                        type = external_stage
                        storage_provider = s3
                        enabled = true
                        storage_aws_role_arn = 'arn:aws:iam::108782091836:role/aws_snowflake_s3_role'
                        storage_allowed_locations = ('s3://useforgenralpurpose/')""")
    
def set_database_schema():
    cur.execute("""drop database if exists sales""")
    cur.execute("""create database sales""")
    cur.execute("""use database sales""")
    cur.execute("""create schema sales.landing""")
    cur.execute("""use schema sales.landing""")
       
def create_parquet_file_format():
    cur.execute("""create or replace file format parquet_ff type=parquet""")

def create_parquet_s3_stage():
    cur.execute(""" CREATE OR REPLACE STAGE s3_parquet
                        URL = 's3://useforgenralpurpose/parquet/'
                        STORAGE_INTEGRATION = s3_int
                        FILE_FORMAT = parquet_ff""")
    
#create_SNF_AWS_S3_INT()
set_database_schema()
create_parquet_file_format()
create_parquet_s3_stage()

#create orders table
cur.execute(""" create or replace table orders 
                    using template(select array_agg(object_construct(*)) 
                        from table(infer_schema(
                                location => '@s3_parquet',
                                files =>'orders.parquet',
                                file_format => 'parquet_ff',
                                ignore_case => true
         ))) """)

#create products table
cur.execute(""" create or replace table products
                    using template(select array_agg(object_construct(*)) 
                        from table(infer_schema(
                                location => '@s3_parquet',
                                files =>'products.parquet',
                                file_format => 'parquet_ff',
                                ignore_case => true
         ))) """)

#create reviews table
cur.execute(""" create or replace table reviews
                    using template(select array_agg(object_construct(*)) 
                        from table(infer_schema(
                                location => '@s3_parquet',
                                files =>'reviews.parquet',
                                file_format => 'parquet_ff'
                                ignore_case => true
         ))) """)