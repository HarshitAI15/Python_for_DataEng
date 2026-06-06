import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

# print(response.status_code)  # 200 means success
# print(type(response.json())) # <class 'list'>
# print(response.json()[0])    # first user


# print(response.json()[0])
# print(response.status_code)   # 200
# print(response.ok)            # True
# print(response.url)           # https://jsonplaceholder.typicode.com/users
# print(response.elapsed.total_seconds())       # 0:00:00.312041 — time taken
# print(response.headers)       # {'Content-Type': 'application/json', ...}
# print(response.text)          # '[{"id":1,"name":"Leanne Graham"...}]' — raw string
# print(response.content)       # b'[{"id":1...' — raw bytes


if response.status_code == 200:
    print(response.json())
    print(f"got {len(response.json())} users")
else:
    print(f"failed Something went wrong status code: {response.status_code}")
    

