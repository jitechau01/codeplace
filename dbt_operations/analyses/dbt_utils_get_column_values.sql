{{ dbt_utils.get_column_values(table=ref('bronze_products'), column='Category', order_by='count(*) desc', max_records=none, default=none, 
where=none) }}

