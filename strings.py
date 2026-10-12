order_id = "ORD-12345"
supplier = "Tech Supplies Inc."
description = "Order for 50 units of gaming laptops"

print(order_id)
print(type(order_id))
print(len(order_id))

tracking_number = "TRK-987654321"
print(tracking_number)
print(tracking_number[-1])
print(tracking_number[3:7])

status="Skipped"
status= "s" + status[1:]
print(status)

status = "in-transit"
clean_status = status.strip()
print(clean_status)

supplier = "Tech Supplies Inc."
clean_supplier = supplier.lower()
print(clean_supplier)

supplier = "TECH Supplies Inc."
clean_supplier = supplier.strip().title()
print(clean_supplier)

message = "Skipping the order due to high demand."
if "delay" in message.lower():
    print("Alert! There is a skipping delay.")
else:
    print("No skipping delay reported.")

order_id = "ORD-12345"
if order_id.startswith("ORD-"):
    print("Valid order ID.")
else:
    print("Invalid order ID.")

supplier_code = "TSI-001, Tech Supplies Inc., Bengaluru"

details = supplier_code.split(",")
#print("Supplier Code: ", details[0])
#print("Supplier Name: ", details[1])
#print("Supplier Location: ", details[2])
status="Active"
location="Chennai"
message=f"Supplier Code: {supplier_code} is {status} from {location}"
print(message)

products = ["laptop", "smartphone", "tablet", "headphones", "telephones"]
summary = ", ".join(products)
print(f"Available Products: {summary}")
order_id = "ORD-12345"
amount = 1500
print(f"Order ID: {order_id}, confirmed total Amount: ${amount:.2f}.")