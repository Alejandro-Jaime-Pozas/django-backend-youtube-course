import requests

headers = {'Authorization': 'Bearer c3017de6c6f94a2598c00146c1e58cf5a76ba8d4'}
endpoint = 'http://localhost:8000/api/products/'

data = {
    'title': "scarf",
    'content': "One maroon and gold colored scarf for first years",
    'price': 29.99
}
# get_response = requests.get(endpoint, json={'product_id': 123}, )
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())