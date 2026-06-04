import os,csv,json

output_folder = r"C:\Users\Mohan lal\Documents\Python_experiment\Day-2 JSON Processing"
os.makedirs(output_folder,exist_ok=True)

# Data to be processes JSON File
data = {
    "platform": "Swiggy",
    "orders": [
        {"order_id": 201, "customer": {"name": "Ravi", "phone": "9876543210"}, "restaurant": {"name": "Pizza Hut", "city": "Delhi"}, "amount": 450, "status": "delivered"},
        {"order_id": 202, "customer": {"name": "Priya"}, "restaurant": {"name": "Burger King", "city": "Mumbai"}, "amount": 300, "status": "delivered"},
        {"order_id": 203, "customer": {"name": "Arjun", "phone": "9123456780"}, "restaurant": {"name": "Dominos"}, "amount": 650, "status": "cancelled"},
        {"order_id": 204, "customer": {"name": "Sneha", "phone": "9988776655"}, "restaurant": {"name": "KFC", "city": "Bangalore"}, "amount": 520, "status": "delivered"},
        {"order_id": 205, "customer": {"name": "Karan"}, "restaurant": {"name": "Subway", "city": "Delhi"}, "amount": 200, "status": "delivered"},
    ]
}

flattened= []
revenue = 0
for order in data["orders"]:
    if order["status"] == "delivered":
        flat = {
            "order_id" : order.get("order_id"),
            "customer_name": order.get("customer").get("name"),
            "phone": order.get("customer").get("phone","N/A"),
            "restaurant_name": order.get("restaurant").get("name"),
            "city": order.get("restaurant").get("city","N/A"),
            "amount": order["amount"]
        }
        revenue += int(order.get("amount"))
        flattened.append(flat)
        
with open(os.path.join(output_folder,"delivered_order.csv"),"w",newline="") as f:
    writer = csv.DictWriter(f,fieldnames=["order_id","customer_name","phone","restaurant_name","city","amount"])
    writer.writeheader()
    writer.writerows(flattened)

print("Total Delivered order:",len(flattened), "\nTotal revenue:", revenue)
      
