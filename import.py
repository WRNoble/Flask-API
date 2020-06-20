import requests
import json

API_URL = "https://api.themoviedb.org/3/collection/10?api_key=32857e29b09b22b340a8f7883f7b7c6d"

request = requests.get(API_URL)
print(request.json())

with open('data.json', 'w') as f:
    json.dump(request.json(), f, indent=2)
    