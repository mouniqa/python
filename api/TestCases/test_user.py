import requests
import json
import jsonpath


def test_create_user():

    url = 'https://reqres.in/api/users'

    file = open('/Users/jagadeesh/mywork/python/api/create_user.json','r')
    data = file.read()

    json_request = json.loads(data)

    response = requests.post(url,json_request)

    assert response.status_code == 204

    json_output = json.loads(response.text)

    timestamp = jsonpath.jsonpath(json_output,'createdAt')
    name = jsonpath.jsonpath(json_output,'name')
    job = jsonpath.jsonpath(json_output,'job')
    id = jsonpath.jsonpath(json_output,'id')

    assert   job[0] == 'Tech Lead'


def test_get_pages():

    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    assert response.status_code == 200

    json_output = json.loads(response.text)

    total_pages = jsonpath.jsonpath(json_output,'total_pages')

    assert total_pages[0] == 2

    print(total_pages[0])






# print(response.text)
