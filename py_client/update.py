import requests

endpoint = 'http://localhost:8000/api/products/3/update/'

data = {
    'title': 'used broom',
    'price': 1499.99,
}

# get_response = requests.get(endpoint, json={'product_id': 123}, )
get_response = requests.put(endpoint, json=data)
print(get_response.json())