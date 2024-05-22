# Atm  with Mysql Database

import mysql.connector

db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="Pratik1506",
                             database="demo")

cur = db.cursor()

# Create table (uncomment to run once)

# cur.execute("CREATE TABLE IF NOT EXISTS ATM (id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(20),pin INT,balance DOUBLE)")
# db.commit()


name = input("Enter your name: ")
pin = int(input("Enter pin: "))
print("Pin set successfully")
acc_balance = 20000

# Insert new user into the ATM table
que = "INSERT INTO ATM (name, pin, balance) VALUES (%s, %s, %s)"
value = (name, pin, acc_balance)
cur.execute(que, value)
db.commit()

def get_balance(name, pin):
    que1 = "SELECT balance FROM ATM WHERE name = %s AND pin = %s"
    value1 = (name, pin)
    cur.execute(que1, value1)
    data = cur.fetchone()
    if data:
        return data[0]
    else:
        return None

def update_balance(name, pin, new_balance):
    que2 = "UPDATE ATM SET balance = %s WHERE name = %s AND pin = %s"
    value2 = (new_balance, name, pin)
    cur.execute(que2, value2)
    db.commit()

def deposit():
    global acc_balance
    amount = int(input("Enter the amount to deposit :-"))
    if amount > 0:
        acc_balance += amount
        update_balance(name, pin, acc_balance)
        print(amount, "has been deposited.")
    else:
        print("Invalid amount. Deposit failed.")

def withdraw():
    global acc_balance
    amount = int(input("Enter the amount to withdraw :-"))
    if amount > 0 and amount <= acc_balance:
        acc_balance -= amount
        update_balance(name, pin, acc_balance)
        print(amount, "has been withdrawn.")
    else:
        print("Invalid amount or insufficient balance. Withdrawal failed.")

while True:
    print(''' *Welcome to the ATM machine*
          1. Withdraw
          2. Deposit
          3. Check balance
          4. Change pin
          5. Exit''')
    choice = int(input("Enter your choice :- "))

    if choice == 1:
        UserPin = int(input("Enter pin: "))
        if UserPin == pin:
            print("Pin entered successfully")
            withdraw()
        else:
            print("Wrong Pin")

    elif choice == 2:
        UserPin = int(input("Enter pin: "))
        if UserPin == pin:
            print("Pin entered successfully")
            deposit()
        else:
            print("Wrong Pin")

    elif choice == 3:
        UserPin = int(input("Enter pin: "))
        if UserPin == pin:
            print("Pin entered successfully")
            current_balance = get_balance(name, pin)
            if current_balance is not None:
                print("Your balance in your account is:- ", current_balance)
            else:
                print("Account not found.")
        else:
            print("Wrong Pin")

    elif choice == 4:
        OldPin = int(input("Enter old pin: "))
        if OldPin == pin:
            NewPin = int(input("Enter new pin: "))
            que3 = "UPDATE ATM SET pin = %s WHERE name = %s AND pin = %s"
            value3 = (NewPin, name, OldPin)
            cur.execute(que3, value3)
            db.commit()
            pin = NewPin
            print("New pin set")
        else:
            print("Wrong Pin")

    elif choice == 5:
        print("Successfully Exited")
        break

    else:
        print("Invalid choice, please select a valid option.")
