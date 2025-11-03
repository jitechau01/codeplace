{{
  config(
    tags='contains_pii'
    )
}}

SELECT
    id,
    created_at,
    city,
    state,
    extract(year from to_date(birth_date)) as birth_year,
    source as sales_channel
FROM
{{ ref('bronze_users') }}