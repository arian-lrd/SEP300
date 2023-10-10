import  requests
response = requests.get("https://dummyjson.com/products")
print(response.json)
