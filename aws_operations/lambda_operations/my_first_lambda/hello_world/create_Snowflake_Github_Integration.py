import snowflake.connector as sf
import os


def lambda_handler(event,context):
    conn=sf.connect(
        account='XQNFMVZ-LWC02945',
        user='guest',
        password=os.getenv('snfpwd'),
        role='accountadmin'
    )
    cur=conn.cursor()
    cur.execute("""use role accountadmin""")
    cur.execute("""use warehouse compute_wh""")
    cur.execute("""drop database if exists sales""")
    cur.execute("""create or replace database sales""")
    cur.execute("""create schema sales.hr""")
    cur.execute("""use schema sales.hr""")

    #create secret
    cur.execute(""" create or replace secret my_github_secret
                    type=password
                    username='jitechau01'
                    password='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' """)

    #create github api integration object
    cur.execute(""" create or replace api integration my_git_api_integration
    api_provider=git_https_api
    api_allowed_prefixes=('https://github.com/jitechau01/')
    allowed_authentication_secrets=(my_github_secret)
    enabled=true """)

    #create git reposiory parallel to 
    cur.execute(""" create or replace git repository my_github_repo
    api_integration=my_git_api_integration
    git_credentials=my_github_secret
    origin='https://github.com/jitechau01/codeplace' """)