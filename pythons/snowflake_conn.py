import snowflake.connector as sf
import os

conn=sf.connect(
        account='XQNFMVZ-LWC02945',
        user='guest',
        password=os.getenv('snfpwd'),
        role='accountadmin'
    )
    
cur=conn.cursor()