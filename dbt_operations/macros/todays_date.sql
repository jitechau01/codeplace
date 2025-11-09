{%- macro todays_date() -%}
  {{ modules.datetime.date.today() }}
{%- endmacro -%}