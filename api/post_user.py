import requests
import json
import jsonpath

url = 'https://reqres.in/api/users'

file = open('/Users/jagadeesh/mywork/python/api/create_user.json','r')
data = file.read()
json_format = json.loads(data)

response = requests.post(url,json_format)

assert response.status_code == 201

print(response.headers.get('Content-Length'))

json_response = json.loads(response.text)

print(json_response)

id = jsonpath.jsonpath(json_response,'id')

print(id[0])

print(type(response.text))
