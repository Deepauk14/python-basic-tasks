from abc import ABC, abstractmethod
from functools import reduce

# ==============================
# Task 2: Abstraction
# ==============================

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


# ==============================
# Base Class
# ==============================

class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id


# ==============================
# Task 1: super()
# ==============================

class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}"


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"


# ==============================
# Sample Data
# ==============================

students = [
    Student("John", 1, "CS", 60000),
    Student("Alice", 2, "IT", 45000),
    Student("Bob", 3, "ECE", 70000)
]

faculty = [
    Faculty("Dr.Smith", 101, 40000),
    Faculty("Dr.Raj", 102, 25000),
    TempFaculty("Dr.Kumar", 103, 35000, "6 months")
]


# ==============================
# Final Challenge
# ==============================

# 1. Print all details
print("ALL DETAILS")
for s in students:
    print(s.get_details())

for f in faculty:
    print(f.get_details())


# ==============================
# Task 3: Sorting
# ==============================

students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)

print("\nSORTED STUDENTS (by fees)")
for s in students:
    print(s.get_details())

print("\nSORTED FACULTY (by salary)")
for f in faculty:
    print(f.get_details())


# ==============================
# Task 4: map()
# ==============================

student_names = list(map(lambda s: s.name, students))
print("\nSTUDENT NAMES:", student_names)


# ==============================
# Task 5: filter()
# ==============================

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("\nHIGH FEE STUDENTS")
for s in high_fee_students:
    print(s.get_details())

print("\nHIGH SALARY FACULTY")
for f in high_salary_faculty:
    print(f.get_details())


# ==============================
# Task 6: reduce()
# ==============================

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("\nTOTAL FEES:", total_fees)
print("TOTAL SALARY:", total_salary)


# ==============================
# Task 7: Higher Order Function
# ==============================

def process_users(users, func):
    return list(map(func, users))


# Example usage
processed_names = process_users(students, lambda s: s.name.upper())
print("\nPROCESSED STUDENT NAMES:", processed_names)
