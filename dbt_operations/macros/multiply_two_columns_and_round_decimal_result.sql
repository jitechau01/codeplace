{% macro multiply_two_columns_and_round_decimal_result(col1,col2,decimal_places=2) -%}
  round({{ col1 }} * {{ col2 }} * {{ decimal_places }})
{% endmacro %}