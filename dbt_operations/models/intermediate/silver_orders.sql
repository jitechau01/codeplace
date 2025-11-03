SELECT
    id,
    to_date(created_at) as order_date,
    user_id,
    product_id,
    quantity,
    unit_price,
    quantity * unit_price as order_amount
FROM {{ ref('bronze_orders')}}