#before execute program
#1. create database demo;
#2. create table to_do_list(id int primary key auto_incremet,task varchar(100),date date)


import mysql.connector
import datetime

db = mysql.connector.connect(host = "localhost",
                             user = "root"  ,
                             password = "Pratik1506" ,
                             database = "demo")

cur = db.cursor()

def Insert():
    y_task = input("Enter a Task :- ")
    def ins():
        xyz=int(input("1.Set Date \n2.Defult (Today)\n \nEnter your choice(1/2) :- "))
        if(xyz==1):
            T_date = datetime.datetime.strptime(input("add date (yyyy-mm-dd):- "), '%Y-%m-%d').date()
        
            if T_date< datetime.date.today():
                print("*********************************************************")
                print("please enter proper date")
                print("*********************************************************")
                ins()    
            else:
                return T_date
        elif(xyz==2):
            T_date =datetime.date.today()
            return T_date
        else:
            print("**************************************************************")
            print("invalid data")
            print("**************************************************************")
            ins()
    T_date=ins()
    que ="insert into to_do_list(date,task)values(%s,%s)"
    values=(T_date,y_task)
    cur.execute(que,values)
    db.commit()
    print("Task is added Successfully !!!!!")
    print("**************************************************************")
    abc1=int(input("Add another Task (1/2) \n1.add\n2.Exit \n Enter your choice :-"))
    if(abc1==1):
        print("**************************************************************")
        Insert()
    elif(abc1==2):
        print("**************************************************************")
        main()
    else:
        pass

def ViewST():
    taskid = int(input("Task id :- "))
    que1="select * from to_do_list where id = %s"
    cur.execute(que1,(taskid,))
    data = cur.fetchone()
    print(data)
    print("**************************************************************")
    abc=int(input("View another Task (1/2) \n1.View\n2.Exit \n Enter your choice :- "))
    if(abc==1):
        print("**************************************************************")
        D=ViewST()
    elif(abc==2):
        print("**************************************************************")
        main()
    else:
        pass

def View_all():
    que2="select * from to_do_list"
    cur.execute(que2)
    data = cur.fetchall()
    for i in data:
        print(i)
    print("**************************************************************")
    main()
def Delete():
    taskid = int(input("Task id :- "))
    que3="delete from to_do_list where id = %s"
    cur.execute(que3,(taskid,))
    db.commit()
    print(" Task is deleted")
    print("**************************************************************")
    abc=int(input("Delete another Task (1/2) \n1.Delete\n2.Exit \n Enter your choice :- "))
    if(abc==1):
        print("**************************************************************")
        Delete()
    elif(abc==2):
        print("**************************************************************")
        main()
    else:
        pass
        
def update():
    taskid = int(input("Task id :- "))
    new_task = input("Enter a Task :- ")
    new_date = datetime.date(input("add date :-"))
    que4="update to_do_list set date =%s,task =%s where id= %s"
    values4=(new_date,new_task,taskid)
    cur.execute(que4,values4)
    db.commit()
    print("Task is updated !!!")
    print("**************************************************************")
    abc=int(input("Update another Task (1/2) \n1.Update\n2.Exit \n Enter your choice :- "))
    if(abc==1):
        print("**************************************************************")
        update()
    elif(abc==2):
        print("**************************************************************")
        main()
    else:
        pass
    
def main():
    choice = 0
    while True:
        print(" ")
        print("1.Add task \n2.View specific task \n3.View all task \n4.Delete \n5:Update \n6:EXIT")
        print(" ")
        choice=int(input("Enter Your Choice :- "))
        if (choice==1):
            Insert()
        elif(choice==2):
            ViewST()
        elif(choice==3):
            View_all()
        elif(choice==4):
            Delete()
        elif(choice==5):
            update()
        elif(choice==6):
            break
        else:
            break

main()
        
