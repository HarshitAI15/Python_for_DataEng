# with open("sample.txt","r") as file:
#     content = file.read()
#     print(content)
    

with open("sample.txt","w") as file:
    file.write("Hello, World! \nHow are you? This is my first file operation in Python.")
    
with open("sample.txt","r") as file:
    content = file.read()
    print(content)

import csv
with open("employee.csv", "w", newline="")  as f:
    writer = csv.writer(f,delimiter="|")
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "Delhi"])
    writer.writerow(["Bob", 25, "Mumbai"])
    writer.writerow(["Charlie", 35, "Bangalore"])
    
with open("employee.csv", "r") as f:
    reader = csv.reader(f, delimiter="|")
    reader1 = csv.DictReader(f, delimiter="|")
    print("\n Below are the content of csv file\n")
    for row in reader1:
        print(row["Name"], int(row["Age"]), row["City"])
        print(row)
        
with open("employee1.csv", "w", newline="") as f:
    writer = csv.DictWriter(f,fieldnames=["Name", "Age", "City"])
    writer.writeheader()
    
    writer.writerow({"Name": "Harshit", "Age": 30, "City": "Delhi"}) 
    writer.writerow({"Name": "Satyam", "Age": 25, "City": "Mumbai"})
    writer.writerow({"Name": "Aryan", "Age": 35, "City": "Bangalore"})

with open("employee1.csv", "r") as f:
    reader = csv.DictReader(f)
    print("\n Below are the content of csv file\n")
    for row in reader:
        print(row["Name"], int(row["Age"]), row["City"])
        print(row)
    

