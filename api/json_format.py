import requests
import json
import jsonpath

url = 'https://reqres.in/api/users?page=2'

response = requests.get(url)

content = response.content

json_format = json.loads(response.text)

print(json_format)

pages = jsonpath.jsonpath(json_format,'total_pages')

assert pages[0]==2
