import mysql.connector as mysql
from mysql.connector import InterfaceError



try:
    db = mysql.connect(host="localhost", user="root", password="", database="bank")
    command_handler = db.cursor(buffered=True)
    print("Data Base connected".center(50))
except InterfaceError as err:
    print(f"Couldn't Connected Database server")
else:
    print("Successfully Connected ".center(50))

# class User:
#     print("")
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def show_details(self):
#         print("Persnal details")
#         print("")
#         print("Name  : ", self.name)
#         print("Age    : ", self.age)
#         print("Gender : ", self.gender)
#
#
# class Bank(User):
#     def __init__(self, name, age, gender):
#         super().__init__(name, age, gender)
#         self.balance = 0
#
#     def deposit(self, amount):
#         self.amount = amount
#         self.balance = self.balance + self.amount
#         print("Balance Updated : $", self.balance)
#
#     def withdraw(self, amount):
#         self.amount = amount
#         if self.amount > self.balance:
#             print(f"Insufficient fund | Now balance is {self.balance}")
#         else:
#             self.balance = self.balance - self.amount
#             print(f"Account balance is update {self.balance}")
#
#     def view_balance(self):
#         self.show_details()
#         print("Balance : $", self.balance)
#

class Working_process:
    def admin_option(self):
        while True:
            print("")
            print("Login success".center(50))

            print("1. User account add :")
            print("2. User account Deleted :")
            print("3. Logout :")
            user_option = input(str("Option : "))

            if user_option == "1":
                acc_number = input(str("Enter account Number : \n"))
                name = input(str("User Name : \n"))
                password = input(str("User password : \n"))
                amount = input(str("Totall ammount : \n"))
                address = input(str("User address  : \n"))

                query_vals = (acc_number, name, password, amount, address)
                command_handler.execute(
                    "INSERT INTO bank_details ( acc_number, name, password, amount, address ) VALUES (%s, %s, %s, %s, %s)",
                    query_vals)
                db.commit()
                print(f"User Name {name} {password} {amount} {address} has been added")

            elif user_option == "2":
                print("")
                print("Existing user delete.".center(50))

                acc_number = input(str("account number : "))
                name = input(str("User name : "))
                query_vals = (acc_number, name)

                command_handler.execute("DELETE FROM bank_details WHERE acc_number = %s AND name = %s ", query_vals)
                db.commit()
                if command_handler.rowcount < 1:
                    print("User not found")
                else:
                    print(f" User {name} Has been deleted")

            elif user_option == "3":
                break
            else:
                print("invalid option crossed")


    def user_option(self,name):
        while True:
            print("")
            print(f"Welcome Bank user {name}")
            print("")

            print("1. Withdraw ")
            print("2. Balance Check ")
            print("3. Deposit ")
            print("4. Logout ")

            user_option = input(str("Option : \n")).lower()


            if user_option == "1":
                print("Withdraw Portal")
                # withdraw_amount = input(str("Amount : \n"))
                query_vals = name
                command_handler.execute("SELECT amount FROM bank_details WHERE name = %s ",query_vals)



            elif user_option == "2":
                print("Balance Check")

            elif user_option == "3":
                print("Deposit")

            elif user_option == "4":
                break
            else:
                print("Not a valid Option chosed")






class Authentication:
    def admin_auth(self):
        print("Welcome admin".center(50))

        username = input(str("Admin User Name : "))
        password = input(str("Admin User Password  : "))

        if username == "limon":
            if password == "limon@123":
                admin = Working_process()
                admin.admin_option()
            else:
                print("invalid password")
        else:
            print(f"User Name {username} & Password {password} not valid ".center(20))

    def user_auth(self):
        print("")
        print("User Login :".center(50))
        name = input(str("Enter Bank user Name  : \n")).lower()
        password = input(str("Enter Bank User Password : \n")).lower()
        query_vals = (name,password)
        command_handler.execute("SELECT * FROM bank_details WHERE name = %s AND password = %s ",query_vals)

        if command_handler.rowcount <= 0:
            print("Log in not recognized ")
        else:
            user = Working_process()
            user.user_option(name)



class Main:
    while True:
        print("Welcome Bank Management System".center(50))
        print("1. Bank Admin ".center(20))
        print("2. Bank User ".center(20))

        user_option = input(str("option : "))

        if user_option == "1":
            admin = Authentication()
            admin.admin_auth()
        elif user_option == "2":
            user = Authentication()
            user.user_auth()
        else:
            print("Invalid option chose")


if __name__ == "__main__":
    Main()
