# re.match() #matching the pattern at the beginning of the string
# re.search() #searching the pattern anywhere in the string
# re.findall() #finding all occurrences of the pattern in the string
# re.sub() #replacing occurrences of the pattern in the string with a specified replacement
# re.fullmatch() #checking if the entire string matches the pattern
# re.split() #splitting the string based on the pattern



# import re

# order_id = "ORD-2026-0001"
# pattern = r"ORD-\d{4}-\d{4}"

# match = re.match(pattern, order_id)

# if match:
#     year = match.group(0)
#     order_number = match.group(0)

#     print(f"Order ID: {order_id} is valid")
#     print("Year:", year)
#     print("Order Number:", order_number)
# else:
#     print(f"Order ID: {order_id} is invalid")




import re

pin = "123456"
pattern = r"\d{6}"

match = re.match(pattern, pin)

if match:
    print(f"PIN: {pin} is valid")
else:
    print(f"PIN: {pin} is invalid")
 