import requests

endpoint = 'http://localhost:8000/api/products/'

data = {
    'title': "This field is done",
    'price': 23.99
}
# get_response = requests.get(endpoint, json={'product_id': 123}, )
get_response = requests.post(endpoint, json=data)
print(get_response.json())