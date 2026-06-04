import json, csv,os

output_folder = r"C:\Users\Mohan lal\Documents\Python_experiment\Day-2 JSON Processing"
os.makedirs(output_folder,exist_ok=True)

data = {
    "company": "TechCorp",
    "employees": [
        {"id": 1, "name": "Alice", "department": {"name": "Engineering", "floor": 3}, "salary": 90000},
        {"id": 2, "name": "Bob", "department": {"name": "Marketing", "floor": 2}, "salary": 55000},
        {"id": 3, "name": "Charlie", "department": {"name": "Engineering", "floor": 3}, "salary": 120000},
        {"id": 4, "name": "Diana", "department": {"name": "HR", "floor": 1}, "salary": 48000},
        {"id": 5, "name": "Eve", "department": {"name": "Engineering", "floor": 3}, "salary": 95000},
    ]
}

flattned = []
for details in data["employees"]:
        flat = {
            "id" : details["id"],
            "name": details["name"],
            "department_name": details["department"]["name"],
            "floor" : details["department"]["floor"],
            "salary": details["salary"]
        }
        flattned.append(flat)

# print(flattned)

with open(os.path.join(output_folder,"engineer.csv"),"w", newline="") as f:
    writer = csv.DictWriter(f,fieldnames=["id","name","department_name","floor","salary"])
    writer.writeheader()
    count = 0
    total_salary = 0
    for employee in flattned:
        if employee["department_name"] == "Engineering":
            writer.writerow(employee)
            count+= 1
            total_salary += int(employee["salary"])
    print("Total Engineer: ",count, "\nAverage salary: ", round(total_salary/count,2))
    
    
    