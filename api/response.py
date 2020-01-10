import requests

url = 'https://reqres.in/api/users?page=2'

response = requests.get(url)
content = response.content
headers = response.headers

print(headers)
print(content)
print(headers)
