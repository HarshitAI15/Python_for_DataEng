import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=999")
print(response.status_code)
print(response.json())