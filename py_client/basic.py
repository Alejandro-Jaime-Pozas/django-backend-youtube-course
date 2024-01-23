import requests

# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/'

get_response = requests.get(endpoint, json={'query': 'hello world'})
print(get_response.text) # print raw text of html document
print(get_response.status_code)

# print(get_response.json())
# print(get_response.status_code)