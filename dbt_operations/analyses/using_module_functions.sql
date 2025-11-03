{% set current_date_time = modules.datetime.datetime.now() %}
{% set todays_date = modules.datetime.date.today() %}
{{ current_date_time }}
{{ todays_date }}