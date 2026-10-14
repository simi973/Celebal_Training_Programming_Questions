# Exercise 1
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    def display_info(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
    def is_passed(self):
        return self.marks >= 40

s1 = Student("Shruti", 101, 85)
s1.display_info()
print("Passed:", s1.is_passed())




# Exercise 2
from uuid import uuid4
class Order:
    def __init__(self, customer_name):
        self.order_id = str(uuid4())
        self.customer_name = customer_name
        self.products = []
    def add_product(self, product, price):
        self.products.append({"product": product, "price": price})
    def display_order_details(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Product List:")
        for item in self.products:
            print(item["product"], "-", item["price"])
        total = sum(item["price"] for item in self.products)
        print("Total:", total)

order1 = Order("Shruti")
order1.add_product("Laptop", 50000)
order1.add_product("Mouse", 500)
order1.add_product("Keyboard", 1500)
order1.display_order_details()



# Exercise 3 
import json
data = {
    "name": "Shruti",
    "city": "Panipat",
    "skills": ["Python", "Java", "SQL"]
}
data["skills"].append("Machine Learning")
data["city"] = "Chandigarh"
json_string = json.dumps(data)
print(json.dumps(data, indent=4))