products = ["laptop", "smartphone", "tablet", "telephones", ]
products.append("monitor")  #add a new profuct
products[0] = "gaming laptop" #updating a product
products.remove("tablet") #removing a product
print(products)
print("watch" in products)

product = ["P1", "Keyboard", 3500]
product_id, name, price = product

#dictonaries of product details

inventory = {
  "P1": {"name": "Keyboard", "price": 3500, "quantity": 50},
  "P2": {"name": "Mouse", "price": 1500, "quantity": 100},
  "P3": {"name": "Monitor", "price": 12000, "quantity": 30}
}
print(inventory)
print(inventory.keys())
print(inventory.values())

online_customers={"Alice", "Bob", "Charlie","David"}
returning_customers={"bob", "Eve", "Frank", "Grace"}
print(online_customers | returning_customers) #union of two sets
print(online_customers & returning_customers) #intersection of two sets
print(online_customers - returning_customers) #difference of two sets
