## Mini Project 1: Employee Management System

employees = []

def add_employee():
name = input("Enter name: ")
age = int(input("Enter age: "))
role = input("Enter role: ")
salary = int(input("Enter salary: "))

emp = {"name": name, "age": age, "role": role, "salary": salary}
employees.append(emp)

def display_employees():
for emp in employees:
print(emp)

def update_employee(name):
for emp in employees:
if emp["name"] == name:
emp["salary"] = int(input("Enter new salary: "))

def delete_employee(name):
for emp in employees:
if emp["name"] == name:
employees.remove(emp)



## Mini Project 2: Student Report Card

def report_card():
name = input("Enter student name: ")
m1 = int(input("Marks 1: "))
m2 = int(input("Marks 2: "))
m3 = int(input("Marks 3: "))

total = m1 + m2 + m3
avg = total / 3

if avg >= 90:
    grade = "A"
elif avg >= 70:
    grade = "B"
else:
    grade = "C"

print("\nReport Card")
print("Name:", name)
print("Total:", total)
print("Average:", avg)
print("Grade:", grade)


## Mini Project 3: Shopping Cart System

cart = []

def add_item():
name = input("Product name: ")
price = int(input("Price: "))
qty = int(input("Quantity: "))

cart.append({"name": name, "price": price, "qty": qty})

def display_cart():
total = 0
for item in cart:
cost = item["price"] * item["qty"]
total += cost
print(item["name"], cost)
print("Total Bill:", total)

def remove_item(name):
for item in cart:
if item["name"] == name:
cart.remove(item)


## Mini Project 4: Login & User Validation

users = {"admin": "1234", "user": "abcd"}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
print("Login Successful")
else:
print("Invalid Credentials")


## Mini Project 5: Unique Visitor Counter

visitors = set()

while True:
name = input("Enter visitor name (or exit): ")
if name == "exit":
break
visitors.add(name)

print("Total Unique Visitors:", len(visitors))


## Mini Project 6: String Formatter Tool

name = input("Enter name: ")
product = input("Enter product: ")

print(name, "bought", product)

text = name + " " + product
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))


## Mini Project 7: Bank Account System

account = {}

def create_account():
name = input("Name: ")
balance = int(input("Balance: "))
account[name] = balance

def deposit(name, amount):
account[name] += amount

def withdraw(name, amount):
if account[name] >= amount:
account[name] -= amount

def check_balance(name):
print("Balance:", account[name])


## Mini Project 8: Voting System

votes = {"A": 0, "B": 0, "C": 0}

for i in range(5):
vote = input("Vote (A/B/C): ")
if vote in votes:
votes[vote] += 1

winner = max(votes, key=votes.get)
print("Winner:", winner)


## Mini Project 9: Course Enrollment System

students = {}

def add_student():
name = input("Student name: ")
courses = input("Enter courses (comma separated): ").split(",")
students[name] = courses

def display_students():
for name, courses in students.items():
print(name, courses)


## Mini Project 10: Number Utility Tool

num = int(input("Enter number: "))

print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hex:", hex(num))

print("With commas: {:,}".format(num))
print("Scientific: {:.2e}".format(num))
