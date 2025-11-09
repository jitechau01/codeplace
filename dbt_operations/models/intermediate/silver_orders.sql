SELECT
    id,
    to_date(created_at) as order_date,
    user_id,
    product_id,
    quantity,
    unit_price,
    --quantity * unit_price as order_amount
    --{# multiply_two_columns('quantity','unit_price') #} as order_amount --use of macro instead of line number 8 
    {{ multiply_two_columns_and_round_decimal_result('quantity','unit_price') }} as order_amount  --use of macro with rounding result instead of line number 8
    
FROM {{ ref('bronze_orders')}}