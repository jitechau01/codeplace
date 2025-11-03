{# printing numbers from 1 to 10 #}
{% set x=[1,2,3,4,5,6,7,8,9,10] %}
{% for val in x %}
    {{ val }}
{%- endfor %}

{# generate select statement for a table #}
{% set columns=adapter.get_columns_in_relation(ref('bronze_orders')) %}
select
{% for column in columns -%}
{{- column.name -}}
{% if not loop.last %},
{%- endif %}
{% endfor -%}
from {{ ref('bronze_orders') }}