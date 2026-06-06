import json , csv, requests, os

output_folder = r"C:\Users\Mohan lal\Documents\Python_experiment\Day-3 API requests"
os.makedirs(output_folder, exist_ok = True)

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    flattned = []
    json_data = response.json()
    for user in json_data:
        flat = {
            "id" : user.get("id", "N/A"),
            "name": user.get("name","N/A"),
            "email": user.get("email","N/A"),
            "phone": user.get("phone","N/A")
        }
        flattned.append(flat)
        
    with open(os.path.join(output_folder,"users.csv"), "w", newline="") as f:
        writer = csv.DictWriter(f,fieldnames = ["id","name","email","phone"])
        writer.writeheader()
        writer.writerows(flattned)
    print("Total users fetched:",len(flattned))    
else:
    print(f"failed: {response.status_code}")