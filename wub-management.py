import mysql.connector as mysql

db = mysql.connect(host="localhost",user="root",password="",database="wub")
command_handler = db.cursor()


def teac_auth():
    print("")
    print("Nurse Log In ".center(50))


########### Admin Start

def admin_session():
    while 1:
        print("")
        print("Admin login success")
        print("")
        print("Admin Menu")

        print("1. Register new Student")
        print("2. Register new Teacher")
        print("3. Existing  Delete Student Account")
        print("4. Existing  Delete Teacher Account")
        print("5. Logout")

        user_option = input(str("Option :"))

        if user_option == "1":
            print("")
            print("Register new student")

            username = input(str("Student Username : "))
            password = input(str("Student Password : "))

            query_vals = (username,password)
            command_handler.execute("INSERT INTO users ( username,password,privilege ) VALUES ( %s,%s,'student')",query_vals)
            db.commit()
            print(username +" has been added")

        elif user_option == "2":
            print("")
            print("Register new teacher")

            username = input(str("Teacher Username : "))
            password = input(str("Teacher Password : "))

            query_vals = (username,password)
            command_handler.execute("INSERT INTO users ( username,password,privilege ) VALUES ( %s,%s,'teacher')",query_vals)
            db.commit()
            print(username +" has been added")

        elif user_option == "3":
            print("")
            print("Existing  Delete Student Account")
            print("")

            username = input(str("Student Username : "))
            query_vals = (username,"student")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " Has been deleted")

        elif user_option == "4":
            print("")
            print("Existing  Delete Teacher Account")
            print("")

            username = input(str("Teacher Username : "))
            query_vals = (username,"teacher")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + "Has been deleted")

        elif user_option == "5":
            break


def admin_auth():
    print("")
    print("Admin Login credentials ")
    print("")

    username = input(str("User Name : "))
    password = input(str("Password : "))

    if username == "admin":
        if password == "limon@123":
            admin_session()
        else:
            print("Password Wrong")
    else:
        print("No Valid information ")


########### Admin End


######### Main function start

def main():
    while 1:
        print("")
        print("Welcome to the World University of Bangladesh")
        print("")

        print("Are you Student, Teacher Admin ( 1, 2, 3 )")
        print("1. Student ")
        print("2. Teacher ")
        print("3. Admin ")

        user_option = input(str("Please choose your number. \n"))

        if user_option == "1":
            print("Student Login")
        elif user_option == "2":
            print("Teacher Login")
        elif user_option == "3":
            print("Admin Login")
            admin_auth()
        else:
            print("No valid login")


######### Main function start

main()


