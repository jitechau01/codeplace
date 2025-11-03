{# printing numbers from 1 to 10
{% set x=[1,2,3,4,5,6,7,8,9,10] %}
{% for val in x %}
    {{ val }}
{%- endfor %}

{# generate select statement for a table#}
{% set columns=['ID','CREATED_AT','USER_ID','PRODUCT_ID','QUANTITY','UNIT_PRICE'] %}
select 
{%- for column in columns %}
{{ column  -}}
{% if not loop.last %}
{{- ',' -}}
{% endif %}
{%- endfor %}
from
{# use ref function#}
{{- ref('bronze_orders') }} #}

{# generate select statement for a table through adaptor dbt object#}
{% set columns = adaptor.get_columns_in_relation(ref('bronze_orders')) %}
{{ columns }}

