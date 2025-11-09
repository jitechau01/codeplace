    {% snapshot products_snapshot %}

    {{
        config(
            target_schema='staging',
            unique_key='id',
            strategy='timestamp',
            updated_at='created_at'
        )
    }}

    select * from {{ source('landing', 'products') }}

    {% endsnapshot %}