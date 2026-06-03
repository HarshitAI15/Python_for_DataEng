import json

# Writing JSON objects to a file
data = {
    "company": "TechCorp",
    "employees": [{"name": "Alice", "role": "Engineer"},{"name": "Bob", "role": "Analyst"}]
}

with open("employee2.json", "w") as f:
    json.dump(data, f, indent=4)  # indent makes it human-readable

# Reading JSON
with open("employee2.json", "r") as f:
    loaded = json.load(f)
    # print(loaded)
    print(loaded["company"])
    print(loaded["employees"][0]["name"],"The", loaded["employees"][0]["role"])
    
    
# json_string = {"name": "Alice", "age": 30, "city": "Delhi"}
# print(type(json.dumps(json_string)))


# json_string1 = '{"name": "Alice", "age": 30, "city": "Delhi"}'
# print(type(json.loads(json_string1)))