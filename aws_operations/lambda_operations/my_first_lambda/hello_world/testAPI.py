import requests
import json
 # For JSON responses

def testAPI(event,context):
    response = requests.get('https://api.github.com/events')
    print(response.status_code)
    print(response.json())