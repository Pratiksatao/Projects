import mysql.connector
db = mysql.connector.connect(host = "localhost",
                             user = "root",
                             password = "Pratik1506",
                             database = "login")

cur = db.cursor()


def reg():
    user_name = input("Enter your name :- ")
    pword = input("Set Your Password (Only 6 char) :- ")
    cword = input("Confirm password :- ")    
    if (len(pword) > 6 and pword == cword ):
        print("Enter Valid Data")
        reg()
    else:
        query = "insert into reg(name,password) values (%s,%s)"
        values = (user_name,pword)
        cur.execute(query,values)
        db.commit()
        print("Registration Successful")
    cur.close()
    db.close()

def login():
    name = input("Enter Username :- ")
    password = input("Enter Password :- ")
    
    query="select * from reg where name = %s AND password = %s"
    value=(name,password)
    cur.execute(query,value)
    result = cur.fetchone()
    if result:
        data=result[0]
        if data == name:
            print("Login successful Welcome ",name)
        else:
            print("invalid username or password")

                




choice=0

while True:
    print("=======================================")
    print(" 1.Register ")
    print(" 2.Login ")
    print("=======================================")
    choice=int(input("Enter Your choice :-"))
    print("=======================================")
    if(choice==1):
        reg()
    elif(choice==2):
        login()
    else:
        break