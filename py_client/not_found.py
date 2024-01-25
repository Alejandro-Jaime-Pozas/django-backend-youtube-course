import requests

endpoint = 'http://localhost:8000/api/products/20898787686687/'

# get_response = requests.get(endpoint, json={'product_id': 123}, )
get_response = requests.get(endpoint)
print(get_response.json())