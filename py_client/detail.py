import requests

endpoint = 'http://localhost:8000/api/products/2/'

# get_response = requests.get(endpoint, json={'product_id': 123}, )
get_response = requests.get(endpoint, json={'title': 'gryffindor', 'content': 'Hello World', 'price': 13.98})
print(get_response.json())