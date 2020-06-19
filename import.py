import request
import json

API_URL = ""

request = requests.get(API_URL)

with open('data.json', 'w') as f:
    json.dump(request.json(), f, indent=2)