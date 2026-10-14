# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def display_info(self):
#         print(f"Product Name: {self.name}, Price: ${self.price:.2f}")

#     def calculate_inventory_value(self, quantity):
#         return self.price * quantity
# product1 = Product("Gaming Laptop", 1200.00)
# product1.display_info()
# print(f"Inventory Value for 10 units: ${product1.calculate_inventory_value(10):.2f}")


# class Warehouse:
#     def __init__(self, name, stock):
#         self.name = name
#         self.stock = stock

#     @property
#     def total_stock(self):
#         return sum(self.stock.values())

#     def add_stock(self, product_id, quantity):
#         if product_id in self.stock:
#             self.stock[product_id] += quantity
#         else:
#             self.stock[product_id] = quantity

#     def remove_stock(self, product_id, quantity):
#         if product_id not in self.stock:
#             raise ValueError("Product not found.")

#         if self.stock[product_id] < quantity:
#             raise ValueError("Insufficient stock.")

#         self.stock[product_id] -= quantity

#         if self.stock[product_id] == 0:
#             del self.stock[product_id]


# warehouse = Warehouse(
#     "Central Warehouse",
#     {"P1": 100, "P2": 200, "P3": 150}
# )

# warehouse.add_stock("P1", 50)
# warehouse.remove_stock("P2", 30)

# print(f"Total Stock in {warehouse.name}: {warehouse.total_stock}")

# class Supplier:
#     def __init__(self, supplier_id, name,):
#         self.supplier_id = supplier_id
#         self.name = name

#     def show_details(self):
#         print(f"Supplier ID: {self.supplier_id}, Name: {self.name}")

# class LocalSupplier(Supplier):
#   def supply(self):
#     print(f"Local Supplier {self.name} is supplying products.")

# class InternationalSupplier(Supplier):
#   def supply(self):
#     print(f"International Supplier {self.name} is supplying products.")

# supplier1 = LocalSupplier("LS-001", "Local Tech Supplies")
# supplier2 = InternationalSupplier("IS-001", "Global Tech Supplies")

# supplier1.show_details()
# supplier1.supply()

# supplier2.show_details()
# supplier2.supply()


class Truck:
    def calculate_cost(self, distance):
        return distance * 20
class AirFreight:
    def calculate_cost (self, distance):
        return distance * 50
class Ship:
    def calculate_cost (self, distance):
        return distance * 10
class Rail:
    def calculate_cost (self, distance):
        return distance * 15

transports = [Truck(), AirFreight(), Ship(), Rail()]
for transport in transports:
    print (transport.calculate_cost(150))