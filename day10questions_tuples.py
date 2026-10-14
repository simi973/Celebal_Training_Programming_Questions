# PROG 3.3: Swapping Variables Using Tuple Packing and Unpacking
def swap(a, b):
    a, b = b, a
    return a, b
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print("\nInitial Value of a & b are")
print("a =", a)
print("b =", b)
x, y = swap(a, b)
print("\nAfter swapping (using function):")
print("x =", x)
print("y =", y)


# PROG 4.1: Manually finding common friends by iterating over two lists.
school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']
common_friends = []
for friend in school_friends:
    if friend in college_friends:
        common_friends.append(friend)
print("Common friends (Iterative method):", common_friends)


# PROG 4.2: Using the & Operator
school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']
common_friends = set(school_friends) & set(college_friends)
print("Common friends (Set & operator):", list(common_friends))


# PROG 4.3: Using the intersection() Method
school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']
common_friends = set(school_friends).intersection(set(college_friends))
print("Common friends (Set intersection method):", list(common_friends))



# PROG 4 : Email Marketing Duplicate Checker for Subscribers and New Sign-ups
current = input("Enter the current subscribers' emails (comma-separated): ")
new = input("Enter the new sign-ups' emails (comma-separated): ")
current_emails = set(current.replace(" ", "").split(","))
new_emails = set(new.replace(" ", "").split(","))
if current_emails.isdisjoint(new_emails):
    print("There are no common email addresses between current subscribers and new sign-ups.")
else:
    common = current_emails.intersection(new_emails)
    print("The following email addresses are present in both lists:", ", ".join(common))



# PROG 5: Employee Access Rights Update Based on Current Staff
access = input("Enter the employees with access rights (comma-separated): ")
current = input("Enter the current employees (comma-separated): ")
access_list = set(name.strip().lower() for name in access.split(","))
current_list = set(name.strip().lower() for name in current.split(","))
access_list.intersection_update(current_list)
print("Updated Access Rights List:")
for name in access_list:
    print(name.capitalize())