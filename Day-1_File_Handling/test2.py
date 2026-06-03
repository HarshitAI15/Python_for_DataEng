import csv

orders = [
    {"order_id": 1, "customer": "Alice", "amount": 1500, "status": "delivered"},
    {"order_id": 2, "customer": "Bob", "amount": 800, "status": "pending"},
    {"order_id": 3, "customer": "Charlie", "amount": 3200, "status": "delivered"},
    {"order_id": 4, "customer": "Diana", "amount": 500, "status": "cancelled"},
    {"order_id": 5, "customer": "Eve", "amount": 2100, "status": "delivered"},
]

with open("orders.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["order_id", "customer", "amount", "status"])
    writer.writeheader()
    for order in orders:
        writer.writerow(order)
        
with open("orders.csv", "r") as f:
    reader = csv.DictReader(f)
    for order in reader:
        if order["status"] == "delivered" and int(order["amount"]) > 1000:
            print(f"{order['customer']} - {order['amount']}")