Task 1: User Info Manager (Functions + Dictionary)
def create_user(name, age, role):
    return {
        "name": name.title(),
        "age": age,
        "role": role
    }

users = []

users.append(create_user("deepauk", 24, "Data Analyst"))
users.append(create_user("arun", 26, "Developer"))
users.append(create_user("kumar", 25, "Tester"))

print("---- USER LIST ----")
for user in users:
    print(user)


 Task 2: Dynamic Calculator (*args)
def calculate_total(*numbers):
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average

total, avg = calculate_total(10, 20, 30, 40)

print("Total:", total)
print("Average:", avg)


 Task 3: Keyword Config System (**kwargs)
def system_config(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")

system_config(mode="debug", version="1.0", theme="dark")


 Task 4: Factorial Service (Recursion)
def factorial(n):
    if n < 0:
        return "Error: Negative numbers not allowed"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
print("Factorial of -3:", factorial(-3))


 Task 5: Memory Optimization (Generator)
def square_generator(n):
    for i in range(n):
        yield i * i

# List version
square_list = [i * i for i in range(5)]
print("List:", square_list)
print("List Type:", type(square_list))

# Generator version
gen = square_generator(5)
print("Generator Type:", type(gen))
print("Generator Output:", list(gen))


 Task 6: Exception Handling Module
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

finally:
    print("Program Completed")


 Task 7: File Handling
# Write to file
file = open("team_data.txt", "w")

users = [
    {"name": "Deepauk", "age": 24, "role": "Data Analyst"},
    {"name": "Arun", "age": 26, "role": "Developer"}
]

for user in users:
    file.write(f"{user['name']}, {user['age']}, {user['role']}\n")

file.close()

print("File closed after writing:", file.closed)

# Read file
file = open("team_data.txt", "r")
content = file.read()
print(content)

file.close()
print("File closed after reading:", file.closed)
