import requests

endpoint = 'http://localhost:8000/api/products/'

data = {
    'title': "scarf",
    'content': "One maroon and gold colored scarf for first years",
    'price': 29.99
}
# get_response = requests.get(endpoint, json={'product_id': 123}, )
get_response = requests.post(endpoint, json=data)
print(get_response.json())