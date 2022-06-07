from turtle import st
import mysql.connector as mysql

db = mysql.connect(host="localhost", user="root", password="", database="hospital")
command_handler = db.cursor(buffered=True)

##### Nurse

def nurse_option():
    while 1:
        print("Nurse Login Succes".center(50))
        print("\n Add Menu\n")

        print("1. Paitent Register")
        # print("2. Doctor Register")
        # print("3. Existing Nurse Delete")
        # print("4. Existing Doctor Delete")
        print("5. Log out")

        user_option = input(str("Option : \n"))

        if user_option == "1":
            print("Patient Register")

        elif user_option == "5":
            break
        else:
            print("No valid option Selected")

def nurse_auth():
    print("")
    print("Nurse Log In ".center(50))
    print("")

    username = input(str("User Name : "))
    password = input(str("Password :"))
    query_vals = (username,password)

    command_handler.execute("SELECT * FROM all_stuff WHERE username = %s AND password = %s AND designation = 'nurse' ",query_vals)
    if command_handler.rowcount <= 0 :
        print("Log in Not Recognize ".center(50))
    else:
        nurse_option()






### Admin
def admin_option():
    while 1:
        print("Admin Login Succes".center(50))
        print("\n Add Menu\n")

        print("1. Nurse Register")
        print("2. Doctor Register")
        print("3. Existing Nurse Delete")
        print("4. Existing Doctor Delete")
        print("5. Log out")

        user_option = input(str("Option : \n"))

        if user_option == "1":

            print("")
            print("Register new Nurse".center(50))

            username = input(str("Nurse Name :\n"))
            password = input(str("Nurse password :\n"))

            query_vals = (username, password)
            command_handler.execute("INSERT INTO all_stuff (username,password,designation) VALUES (%s,%s,'nurse')",
                                    query_vals)
            db.commit()
            print(username + " has been added")


        elif user_option == "2":
            print("")
            print("Doctor Register".center(50))

            username = input(str("Doctor Name : "))
            password = input(str("Doctor Password : "))
            query_vals = (username, password)

            command_handler.execute("INSERT INTO all_stuff (username,password,designation) VALUES (%s,%s,'Doctor')",
                                    query_vals)
            db.commit()
            print(username, " Doctor has been added")

        elif user_option == "3":
            print("")
            print("Existing Nurse Delete")

            username = input(str("Existing Nurse Name : "))
            query_vals = (username, 'nurse')

            command_handler.execute("DELETE FROM all_stuff WHERE username = %s AND designation = %s ", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User Not Found".center(50))
            else:
                print(username, " Deleted".center(50))


        elif user_option == "4":
            print("")
            print("Existing Doctor Delete")

            username = input(str("Existing Doctor Name : "))
            query_vals = (username, 'doctor')

            command_handler.execute("DELETE FROM all_stuff WHERE username = %s AND designation = %s ", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User Not Found".center(50))
            else:
                print(username, " Deleted".center(50))

        elif user_option == "5":
            break
        else:
            print("No Valid Option Selected")



def admin_auth():
    print("")
    print("\nAdmin Login ".center(50))

    admin_user = input(str("Admin User Name :"))
    admin_password = input(str("Admin User Password :"))

    if admin_user == "limon":
        if admin_password == "limon@123":
            admin_option()
        else:
            print("\n Password Incorrect")
    else:
        print("\n Invalid UserName & Password")


def Main():
    while True:
        print("")
        print(" Welcome hospital Management System ".center(50))
        print("1. Nurse ")
        print("2. Doctor ")
        print("3. Admin ")

        user_option = input(str("Option : \n"))

        if user_option == "1":
            nurse_auth()
        elif user_option == "2":
            print("Welcome Doctor")
        elif user_option == "3":
            admin_auth()
        else:

            print("You are selected invalid option")


Main()
