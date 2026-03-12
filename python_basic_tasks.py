# PYTHON BASIC TASKS

# Task 1 – Print Formatting
# Print the following output using sep and end.
# Expected Output:
# Hello World Welcome Python
# Laptop | Mouse | Keyboard

print("Hello", "World", "Welcome", "Python", sep=" ")
print("Laptop", "Mouse", "Keyboard", sep=" | ")


# Task 2 – Variables
# Create variables:
# name = "Ravi"
# age = 22
# city = "Chennai"
# Print them in one line separated by -

name = "Ravi"
age = 22
city = "Chennai"

print(name, age, city, sep="-")


# Task 3 – Multiple Assignment
# Assign values using multiple assignment
# name = "Meena"
# age = 20
# student = True

name, age, student = "Meena", 20, True

print("Name:", name)
print("Age:", age)
print("Student:", student)


# Task 4 – Indexing
# Given: word = "Python"
# Print first letter, third letter, and last letter

word = "Python"

print("First letter:", word[0])
print("Third letter:", word[2])
print("Last letter:", word[-1])


# Task 5 – Arithmetic Operators
# Calculate and print the following operations

print("25 + 10 =", 25 + 10)
print("50 - 20 =", 50 - 20)
print("8 * 5 =", 8 * 5)
print("100 / 10 =", 100 / 10)
print("10 % 3 =", 10 % 3)
print("2 ** 4 =", 2 ** 4)
print("20 // 3 =", 20 // 3)


# Task 6 – BODMAS Expression
# Find the result of the following expression

print(3 + 2 * 5 ** 2)


# Task 7 – Assignment Operator

num = 50
num += 25
print("Final value:", num)

num = 100
num /= 10
print("Result:", num)


# Task 8 – Comparison Operators

print(10 > 5)
print(20 < 15)
print(5 == 5)
print(10 != 8)
print(7 >= 7)
print(6 <= 2)


# Task 9 – String Comparison

a = "apple"
b = "Apple"

print(a == b)


# Task 10 – Logical Operators

print(10 > 5 and 5 == 5)
print(5 > 10 or 10 == 10)
print(not(5 > 2))


# Task 11 – Membership Operator

numbers = [10, 20, 30, 40, 50]

print(20 in numbers)
print(60 in numbers)
print(30 not in numbers)


# Task 12 – Swap Variables

a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)


# Task 13 – Bitwise XOR

a = 6
b = 3

print("a ^ b =", a ^ b)
