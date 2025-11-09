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
    
def set_context():
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

def create_parquet_retail_tables():
    cur.execute(""" create or replace table orders 
                    using template(select array_agg(object_construct(*)) 
                        from table(infer_schema(
                                location => '@s3_parquet',
                                files =>'orders.parquet',
                                file_format => 'parquet_ff',
                                ignore_case => true
         ))) """)
    cur.execute(""" create or replace table products
                    using template(select array_agg(object_construct(*)) 
                        from table(infer_schema(
                                location => '@s3_parquet',
                                files =>'products.parquet',
                                file_format => 'parquet_ff',
                                ignore_case => true
         ))) """)
    cur.execute(""" create or replace table reviews
                    using template(select array_agg(object_construct(*)) 
                        from table(infer_schema(
                                location => '@s3_parquet',
                                files =>'reviews.parquet',
                                file_format => 'parquet_ff',
                                ignore_case => true
         ))) """)
    cur.execute(""" create or replace table users 
                    using template(select array_agg(object_construct(*)) 
                        from table(infer_schema(
                                location => '@s3_parquet',
                                files =>'users.parquet',
                                file_format => 'parquet_ff',
                                ignore_case => true
         ))) """)
    
def create_pqt_select_query_procedure():
    result=cur.execute(""" create or replace procedure sales.landing.sp_pqt_file_select_query(table_name varchar,stage_name varchar)
                    returns varchar
                    language sql
                    as
                    begin
                    desc table IDENTIFIER(:table_name);
                    LET res RESULTSET := (SELECT "name" as column_name,"type" as data_type from Table(result_scan(last_query_id())));
                    LET c1 CURSOR FOR res;
                    let record_value := '';
                    for record  in c1 do
                    record_value := record_value||','||'$1'||':'||record.column_name||'::'||record.data_type||' as '||record.column_name;
                    end for;
                    record_value := 'select '||Right(record_value,length(record_value)-1)||' from '||:stage_name||'/'||:table_name||'.parquet';
                    return record_value;
                    end """)
    
def load_landing_parquet_tables():
    cur.execute(""" truncate table orders """)
    cur.execute(""" truncate table products """)
    cur.execute(""" truncate table users """)
    cur.execute(""" truncate table reviews """)

    #load orders table
    cur.execute(""" copy into orders from
                    ( select $1:id::number(38,0) as id,$1:created_at::timestamp_ntz(9) as created_at,$1:user_id::number(38,0) 
                        as user_id,$1:product_id::number(38,0) as product_id,$1:quantity::number(38,0) as quantity,
                        $1:unit_price::number(34,6) as unit_price from @s3_parquet/orders.parquet) """)
    
    #load products table
    cur.execute(""" copy into products from
                    (select $1:id::number(38,0) as id,$1:created_at::timestamp_ntz(9) as created_at,
                        $1:title::varchar(16777216) as title,$1:category::varchar(16777216) as category,
                        $1:ean::varchar(16777216) as ean,$1:vendor::varchar(16777216) as vendor,
                        $1:price::number(34,6) as price from @s3_parquet/products.parquet) """)
    
    #load users table
    cur.execute(""" copy into users from
                    (select $1:id::number(38,0) as id,$1:created_at::timestamp_ntz(9) as created_at,
                        $1:name::varchar(16777216) as name,$1:email::varchar(16777216) as email,
                        $1:city::varchar(16777216) as city,$1:state::varchar(16777216) as state,
                        $1:zip::varchar(16777216) as zip,$1:birth_date::varchar(16777216) as birth_date,
                        $1:source::varchar(16777216) as source from @s3_parquet/users.parquet) """)

    #load reviews table
    cur.execute(""" copy into reviews from
                    (select $1:id::number(38,0) as id,$1:created_at::timestamp_ntz(9) as created_at,
                         $1:reviewer::varchar(16777216) as reviewer,$1:product_id::number(38,0) as product_id,
                        $1:rating::number(38,0) as rating,$1:body::varchar(16777216) as body from @s3_parquet/reviews.parquet) """)    
    
#create_SNF_AWS_S3_INT()
set_context()
create_parquet_file_format()
create_parquet_s3_stage()
create_parquet_retail_tables()
create_pqt_select_query_procedure()
load_landing_parquet_tables()