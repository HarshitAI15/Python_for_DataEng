import json
import logging

logging.basicConfig(level=logging.INFO)

products = [
    {"id": 1, "name": "Laptop", "price": 80000},
    {"id": 2, "name": "Phone", "price": 40000},
    {"id": 3, "name": "Tablet", "price": 30000},
]

with open("products.json", "w") as f:
    json.dump(products, f, indent=4)
    logging.info("Products have been written successfully to products.json")


with open("products.json", "r") as f:
    loaded_products = json.load(f)
    logging.info("Products have been loaded successfully from products.json")
    
for product in loaded_products:
    logging.info(f"Product1 checking: {product['name']} with price {product['price']}")
    if product["price"] > 35000:
        print(product["name"])
        
    
