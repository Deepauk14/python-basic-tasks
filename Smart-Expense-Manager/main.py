import mysql.connector
from functools import reduce
from abc import ABC, abstractmethod


class BaseExpense(ABC):

    @abstractmethod
    def add_expense(self):
        pass

    @abstractmethod
    def view_expense(self):
        pass


class User:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Expense(User, BaseExpense):

    def __init__(self, name):
        super().__init__(name)

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR_PASSWORD",
            database="expense_db"
        )
        self.cursor = self.conn.cursor()

    def add_user(self):
        query = "INSERT INTO users (name) VALUES (%s)"
        self.cursor.execute(query, (self.get_name(),))
        self.conn.commit()
        print("User Added")

    def add_expense(self, user_id, amount, category, desc, date):
        query = """INSERT INTO expenses 
                   (user_id, amount, category, description, date) 
                   VALUES (%s, %s, %s, %s, %s)"""
        self.cursor.execute(query, (user_id, amount, category, desc, date))
        self.conn.commit()
        print("Expense Added")

    def view_expense(self, user_id):
        query = """
        SELECT u.name, e.amount, e.category, e.description, e.date
        FROM users u
        JOIN expenses e ON u.user_id = e.user_id
        WHERE u.user_id = %s
        """
        self.cursor.execute(query, (user_id,))
        data = self.cursor.fetchall()

        print("\nAll Expenses:")
        for row in data:
            print(row)

        return data

    def filter_by_category(self, data, category):
        return list(filter(lambda x: x[2] == category, data))

    def filter_by_date(self, data, date):
        return [x for x in data if str(x[4]) == date]

    def total_expense(self, data):
        amounts = list(map(lambda x: x[1], data))
        return reduce(lambda a, b: a + b, amounts, 0)

    def category_wise(self, data):
        categories = {x[2] for x in data}

        return {
            cat: sum([x[1] for x in data if x[2] == cat])
            for cat in categories
        }

    def monthly_report(self, data):
        report = {}
        for x in data:
            month = str(x[4])[:7]
            report[month] = report.get(month, 0) + x[1]
        return report

    def highest_expense(self, data):
        return reduce(lambda a, b: a if a[1] > b[1] else b, data)

    def smart_insight(self, data):
        cat_data = self.category_wise(data)
        highest = max(cat_data, key=cat_data.get)
        return f"You are spending too much on {highest}"

    def delete_expense(self, exp_id):
        self.cursor.execute("DELETE FROM expenses WHERE exp_id = %s", (exp_id,))
        self.conn.commit()
        print("Deleted")

    def update_expense(self, exp_id, amount):
        self.cursor.execute("UPDATE expenses SET amount = %s WHERE exp_id = %s", (amount, exp_id))
        self.conn.commit()
        print("Updated")


def menu():
    name = input("Enter your name: ")
    obj = Expense(name)

    data = []

    while True:
        print("\nSmart Expense Manager")
        print("1. Add User")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Filter by Category")
        print("5. Filter by Date")
        print("6. Total Expense")
        print("7. Category-wise Spending")
        print("8. Monthly Report")
        print("9. Highest Expense")
        print("10. Smart Insight")
        print("11. Delete Expense")
        print("12. Update Expense")
        print("13. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            obj.add_user()

        elif choice == "2":
            uid = int(input("User ID: "))
            amt = float(input("Amount: "))
            cat = input("Category: ")
            desc = input("Description: ")
            date = input("Date (YYYY-MM-DD): ")
            obj.add_expense(uid, amt, cat, desc, date)

        elif choice == "3":
            uid = int(input("User ID: "))
            data = obj.view_expense(uid)

        elif choice == "4":
            cat = input("Category: ")
            print(obj.filter_by_category(data, cat))

        elif choice == "5":
            date = input("Date (YYYY-MM-DD): ")
            print(obj.filter_by_date(data, date))

        elif choice == "6":
            print("Total:", obj.total_expense(data))

        elif choice == "7":
            print(obj.category_wise(data))

        elif choice == "8":
            print(obj.monthly_report(data))

        elif choice == "9":
            print("Highest:", obj.highest_expense(data))

        elif choice == "10":
            print(obj.smart_insight(data))

        elif choice == "11":
            exp_id = int(input("Expense ID: "))
            obj.delete_expense(exp_id)

        elif choice == "12":
            exp_id = int(input("Expense ID: "))
            amt = float(input("New Amount: "))
            obj.update_expense(exp_id, amt)

        elif choice == "13":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
