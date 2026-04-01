
# Task 1: Encapsulation


class UserEncap:
    def __init__(self):
        self.__user_name = None
        self.__pwd = None

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name   # password hidden

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")


# Test Task 1
u1 = UserEncap()
u1.set_user("john", "1234")
u1.register()
u1.login()



# Task 2: Inheritance


class User:
    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged In")


class Student(User):
    def student_greet(self):
        print("Hello Student")


class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty):  # Multilevel Inheritance
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


# Test Task 2
s = Student()
s.register()
s.login()
s.student_greet()

f = Faculty()
f.register()
f.faculty_greet()

t = TempFaculty()
t.register()
t.faculty_greet()
t.tempFaculty_greet()

# Parent cannot access child methods
# u = User()
# u.student_greet()  # This will raise an error



# Task 3: Method Overriding


class UserOverride:
    def greet(self):
        print("Welcome User")


class StudentOverride(UserOverride):
    def greet(self):
        print("Welcome Student")


class FacultyOverride(UserOverride):
    def greet(self):
        print("Welcome Faculty")


# Test Task 3
s2 = StudentOverride()
f2 = FacultyOverride()

s2.greet()
f2.greet()



# Task 4: Method Chaining


class UserChain:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self


# Test Task 4
uc = UserChain()
uc.login().greet().register()



# Task 5: Combined Real-Time System


class UserSystem:
    users_count = 0

    def __init__(self, name, pwd):
        self.__name = name
        self.__pwd = pwd
        UserSystem.users_count += 1

    def get_name(self):
        return self.__name

    def register(self):
        print(f"{self.__name} registered")
        return self

    def login(self):
        print(f"{self.__name} logined")
        return self

    def greet(self):
        print("Welcome User")
        return self


class StudentSystem(UserSystem):
    def greet(self):
        print("Welcome Student")
        return self


class FacultySystem(UserSystem):
    def greet(self):
        print("Welcome Faculty")
        return self


# Test Task 5
user1 = StudentSystem("john", "123")
user2 = FacultySystem("admin", "999")

user1.login().greet().register()
user2.login().greet().register()

print("Total Users:", UserSystem.users_count)
