import requests
import json
import jsonpath

url = 'https://reqres.in/api/users/2'

file = '/Users/jagadeesh/mywork/python/api/update_user.json'

with open(file) as f:
    data = f.read()

json_input = json.loads(data)


response = requests.put(url,json_input)

json_output = json.loads(response.text)

assert response.status_code == 200

print(response.text)
print(json_output)

update_timestamp = jsonpath.jsonpath(json_output,'updatedAt')
print(update_timestamp[0])
