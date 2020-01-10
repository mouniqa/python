import requests
import json,jsonpath


def test_pages():
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    assert response.status_code == 200
    json_output = json.loads(response.text)
    print(json_output)
    total_pages = jsonpath.jsonpath(json_output,'total_pages')
    assert total_pages[0] == 2
    print(total_pages[0])

def test_urls():
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    assert response.status_code == 201
    json_output = json.loads(response.text)
    print(json_output)
    total_pages = jsonpath.jsonpath(json_output,'total_pages')
    assert total_pages[0] == 2
    print(total_pages[0])
