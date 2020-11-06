from apiclient.discovery import build
from googleapiclient.discovery import build
import json

my_api_key = "AIzaSyCFZWHPLT3Jjz8plycCdJIpD1ONu4tIqWE"
my_cse_id = '2c7acc6bae33119b6'

def ExecuteSearch(topic,website):

    search = topic +" - "+website

    resourse = build("customsearch", 'v1', developerKey=my_api_key).cse()
    result = resourse.list(q=search, cx=my_cse_id).execute()

    json_object = json.dumps(result['items'])
    with open("links.json", "w") as write:
        write.write(json_object)