import sqlite3

connection = sqlite3.connect('library.db')

cursor = connection.cursor()

def user_exist(name_,lastname,mail):
    cursor.execute("SELECT * FROM users where name_ = ? AND lastname = ? AND mail = ? ", (name_,lastname,mail,))
    finding_one = cursor.fetchall()
    if len(finding_one) == 1:
        # The user exist
        return True
    else:
        return False

def add_user(name_,lastname,mail, address, sex, age):
    if user_exist(name_,lastname,mail):
        print("User already exist")
    else:
        cursor.execute("INSERT INTO users(name_,lastname,mail, address, sex, age)VALUES (?,?,?,?,?,?)", (name_, lastname, mail, address, sex, age,))
        connection.commit()
        print("User created")

def remove_user(name_,lastname,mail):
    if user_exist(name_,lastname,mail):
        cursor.execute("DELETE FROM users WHERE name_ = ? AND lastname = ? AND mail = ?", (name_,lastname,mail,))
        connection.commit()
    else:
        print("User doesn't exist")

def update_user(name_,lastname,mail):
    if user_exist(name_, lastname, mail):
        choice = input("What do you want to modify ? name/lastname/mail/address/sex/age")
        if choice == "name":
            modification = input("Enter a new name")
            cursor.execute("UPDATE users SET name_ = ? WHERE name_ = ? AND lastname = ? AND mail = ? ", (modification,name_,lastname,mail,))
            connection.commit()
        if choice == "lastname":
            modification = input("Enter a new name")
            cursor.execute("UPDATE users SET lastname = ? WHERE name_ = ? AND lastname = ? AND mail = ? ", (modification,name_,lastname,mail,))
            connection.commit()
        if choice == "mail":
            modification = input("Enter a new name")
            cursor.execute("UPDATE users SET mail = ? WHERE name_ = ? AND lastname = ? AND mail = ? ", (modification,name_,lastname,mail,))
            connection.commit()
        if choice == "address":
            modification = input("Enter a new name")
            cursor.execute("UPDATE users SET address = ? WHERE name_ = ? AND lastname = ? AND mail = ? ", (modification,name_,lastname,mail,))
            connection.commit()
        if choice == "sex":
            modification = input("Enter a new name")
            cursor.execute("UPDATE users SET sex = ? WHERE name_ = ? AND lastname = ? AND mail = ? ", (modification,name_,lastname,mail,))
            connection.commit()
        if choice == "age":
            modification = input("Enter a new name")
            cursor.execute("UPDATE users SET age = ? WHERE name_ = ? AND lastname = ? AND mail = ? ", (modification,name_,lastname,mail,))
            connection.commit()

def print_user_list():

    cursor.execute("SELECT * FROM users")
    every_users = cursor.fetchall()
    for user in every_users:
        print(f"{user[0]} : {user[1]} : {user[2]} : {user[3]} : {user[4]} : {user[5]} : {user[6]}")
