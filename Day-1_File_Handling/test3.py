import csv,json

students = [
    {"id": 1, "name": "Ravi", "marks": 88, "city": "Delhi"},
    {"id": 2, "name": "Priya", "marks": 45, "city": "Mumbai"},
    {"id": 3, "name": "Arjun", "marks": 72, "city": "Bangalore"},
    {"id": 4, "name": "Sneha", "marks": 91, "city": "Delhi"},
    {"id": 5, "name": "Karan", "marks": 38, "city": "Mumbai"},
]

with open("students.json", "w") as f:
    json.dump(students,f,indent=4)

with open("students.json", "r") as f:
    loaded_students = json.load(f)
    with open("passed_students.csv", "w", newline="") as f1:
        writer = csv.DictWriter(f1,fieldnames=["id", "name", "marks", "city"])
        writer.writeheader()
        count_passed = 0
        for student in loaded_students:
            if student["marks"]>= 50:
                writer.writerow(student)
                count_passed += 1
        
    print("Passed students have been written to passed_students.csv")
    print("Total passed: ",count_passed)
            
