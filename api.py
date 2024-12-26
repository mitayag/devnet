import requests
import json
response = requests.get("https://fakestoreapi.com/products/1")
data=response.json()
beautified_output=json.dumps(data,indent=4)
print(beautified_output)