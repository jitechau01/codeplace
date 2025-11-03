{%- set temperature = -10 -%}
{%- if temperature > 0 -%}
{{ 'temperature is good to go' }}
{%- elif temperature ==0 -%}
{{ 'temperature is normal' }}
{%- else -%}
{{ 'temperature is negative' }}
{%- endif -%}