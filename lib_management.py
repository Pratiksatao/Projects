#     Before Execute This Program

#     steps:- 
#1.Create Database :-
#   Create Database lib;
#   use lib;
#2.library table:-
#   create table library1(id int primary key auto_increment,name varchar(50),author varchar(50),price float,type varchar(50));
#3.admin table username and password:-
#   create table admin1(username varchar(50),password varchar(50));

import re
import mysql.connector

db = mysql.connector.connect(host = "localhost",
                             user = "root"  ,
                             password = "Pratik1506" ,
                             database = "lib")

cur = db.cursor()


gap=" "*3

class admin:
    def login(self):
        print(" ")
        name = input("Enter Your Name :- ")
        password = input("Enter Your Password :- ")
        print("*******************************************************************************")
        que="select password,username from admin1 where username = %s"
        values = (name,)
        cur.execute(que,values)
        result = cur.fetchone()
        if result:
            data=result[0]
            if data == password:
                
                print("Login successful Welcome ",name)
                self.adata()
        else:
            print("invalid username or password")
            
    def Insert(self):
        bname = input("Enter Book Name :-")
        aname = input("Enter Author Name :-")
        price = float(input("Enter the Price :-"))
        btype = input("Enter Book Type :-")
        
        que1="insert into library1(name,author,price,type)values(%s,%s,%s,%s)"
        values1=(bname,aname,price,btype)
        cur.execute(que1,values1)
        db.commit()
        print("New BooK Added TO the Library")
        abc=int(input("Add another Book (1/2) \n1.add\n2.Exit\nEnter your choice :- "))
        if(abc==1):
            self.Insert()
        else:
            self.adata()

    def Update(self):
        print("                               Select Your Option                                            ")
        print("------------------------------------------------------------------------------------------")
        print("           ID   BOOK NAME          BOOK AUTHOR               PRICE       TYPE")
        print("------------------------------------------------------------------------------------------")
        cur.execute("select * from library1")
        data = cur.fetchall()
        for row in data:
            rec=f"{row[0]}{gap}{row[1]:18s}{gap}{row[2]:20s}{gap}{row[3]:<10.2f}{gap}{row[4]:15s}"
            print(rec.center(100))
        print("------------------------------------------------------------------------------------------")
        
        abc=int(input("1.Update Entire Row \n2.Update Selected Row\n3.Exit\nEnter your choice :- "))
        if(abc==1):
            bid = int(input("Enter Book Id You Want To Update :-"))
            bname = input("Enter New Book Name :-")
            aname = input("Enter New Author Name :-")
            price = float(input("Enter the New Price :-"))
            btype = input("Enter New Book Type :-")
            
            que2="update library1 set name =%s,author=%s,price = %s,type=%s where id= %s"
            values2=(bname,aname,price,btype,bid)
            cur.execute(que2,values2)
            db.commit()
            print("Your Book has been Updated")  
            self.Display() 
        elif(abc==2):
            self.inside_update()
        else:
            pass
        
    def inside_update(self):
        choice=0
        while True:
            print(" ")
            print("*******************************************************************************")
            print(" ")
            print("1.Name     2.Author    3.Price    4.Type   5:EXIT")
            print(" ")
            choice=int(input("Enter Your Choice :- "))
            if(choice==1):
                bid = int(input("Enter Book Id You Want To Update :-"))
                bname = input("Enter New Book Name :-")
                que11="update library1 set name =%s where id= %s"
                values11=(bname,bid)
                cur.execute(que11,values11)
                db.commit()
                print("Your Book Name has been Updated")  
                self.Display()
            elif(choice==2):
                bid = int(input("Enter Book Id You Want To Update:-"))
                bname = input("Enter Book Name You Want To Update:-")
                aname = input("Enter New Author Name :-")
                que12="update library1 set author=%s where id= %s and name=%s"
                values12=(aname,bid,bname)
                cur.execute(que12,values12)
                db.commit()
                print("Your Author Name has been Updated")  
                self.Display()
            elif(choice==3):
                bid = int(input("Enter Book Id You Want To Update:-"))
                bname = input("Enter Book Name You Want To Update:-")
                price = float(input("Enter New Book Price :-"))
                que13="update library1 set pricer=%s where id= %s and name=%s"
                values13=(price,bid,bname)
                cur.execute(que13,values13)
                db.commit()
                print("Your Book Price has been Updated")  
                self.Display()
            elif(choice==4):
                bid = int(input("Enter Book Id You Want To Update:-"))
                bname = input("Enter Book Name You Want To Update:-")
                btype = input("Enter New Book Type :-")
                que14="update library1 set type=%s where id= %s and name=%s"
                values14=(btype,bid,bname)
                cur.execute(que14,values14)
                db.commit()
                print("Your Book Type has been Updated")  
                self.Display()
            elif(choice==5):
                self.adata()
            else:
                pass
                

        
            
    def Delete(self):
        bid = int(input("Enter Book Id :-"))
        aname = input("Enter Author Name :-")
        que3="delete from library1 where id= %s and name=%s"
        values3=(bid,aname)
        cur.execute(que3,values3)
        db.commit()
        print("Your Book has been Deleted")
        abc=input("Delete another Book (1/2) \n1.Delete              2.Exit \n Enter your choice :- ")
        if(abc==1):
            self.Delete()
        else:
            self.Display()
    def Display(self):
        print("           ID   BOOK NAME          BOOK AUTHOR               PRICE       TYPE")
        print("------------------------------------------------------------------------------------------")
        cur.execute("select * from library1")
        data = cur.fetchall()
        for row in data:
            rec=f"{row[0]}{gap}{row[1]:18s}{gap}{row[2]:20s}{gap}{row[3]:<10.2f}{gap}{row[4]:15s}"
            print(rec.center(100))
        self.adata()
    
    def orders(self):
        print("Comming Soon 😁")
        
    def scustomers(self):
        print("Comming Soon 😁")
            
    def adata(self):
        choice = 0
        while True:
            print(" ")
            print("*******************************************************************************")
            print(" ")
            print("1.Insert     2.Update    3.Delete    4.Display   5:SHOW CUSTOMERS    6:ORDERS    7:EXIT")
            print(" ")
            choice=int(input("Enter Your Choice :- "))


            if(choice==1):
                self.Insert()
            elif(choice==2):
                self.Update()
            elif(choice==3):
                self.Delete()
            elif(choice==4):
                self.Display()
            elif(choice==5):
                self.scustomers()
            elif(choice==6):
                self.orders()
            elif(choice==7):
                main()
            else:
                break




class customer:
    
    def check_pword(self,cpword):
        
        if len(cpword)<8:
            return False
        
        if not re.search(r'[A-Z]',cpword):
            return False
        
        if not re.search(r'[a-z]',cpword):
            return False
        
        if not re.search(r'\d',cpword):
            return False
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]',cpword):
            return False
        
        return True
        
        
    
    def reg(self):
        cname=input("Enter Your Name :- ")
        email = input("Enter Your Email :- ")
        
        print(" ")
        print("Set Password with one uppercase, one lowercase, one number, one special char and at least 8 digit")
        print(" ")
        cpword = input("Set Your Password :- ")
        
        def set_pword():
            if self.check_pword(cpword):
                print("Password Set Successfully")
                return cpword
            else:
                print("Invalid data added set password again")
        cpword = set_pword()    
        
        cnumber = int(input("Enter Your Contact Number :- "))
        
        que = "insert into reglogin1(name,email,password,contact)values(%s,%s,%s,%s)"
        value=(cname,email,cpword,cnumber)
        cur.execute(que,value)
        db.commit()
        
        print("Registration Successful !!!")
        
        self.cdata()
            
    def Display(self):
        print("           ID   BOOK NAME          BOOK AUTHOR               PRICE       TYPE")
        print("------------------------------------------------------------------------------------------")
        cur.execute("select * from library1")
        data = cur.fetchall()
        for row in data:
            rec=f"{row[0]}{gap}{row[1]:18s}{gap}{row[2]:20s}{gap}{row[3]:<10.2f}{gap}{row[4]:15s}"
            print(rec.center(100))

    
    
    def login(self):
        print("*******************************************************************************")
        mail=input("Enter Your Email :- ")
        password=input("Enter Your Password :- ")
        
        
        que="select * from reglogin1 where password=%s and email=%s"
        value=(password,mail)
        cur.execute(que,value)
        data=cur.fetchone()
        print(data)
        if data:
            print("Login successful Welcome" )
            self.Display()
            self.inlogin()
        else:
            print("invalid username or password try again")
            self.login()
            
    def inlogin(self):
        choice=0
        while True:
            print(" ")
            print("*******************************************************************************")
            print(" ")
            print("                1.Order Book       2.Go To Cart     3:EXIT")
            print(" ")
            choice=int(input("Enter Your Choice :- "))
            if (choice==1):
                self.order_book()
                
            elif(choice==2):
                self.cart()
                
            elif(choice==3):
                pass
            else:
                print("******************")
                print("Enter Valid Choice")
                self.inlogin()
    
    
    
    
    def payment(self):
        self.cart_display()
        
        tamount=1200.12
        print("Total Amount of Your Order is ",tamount," Rs only")
        choice=0
        while True:
            print(" ")
            print("*******************************************************************************")
            print(" ")
            print("                1.Complete Payment          2:Back")
            print(" ")
            choice=int(input("Enter Your Choice :- "))
            if (choice==1):
                print("Payment Successful !!!!!")
                
            elif(choice==2):
                self.cart()
        
    
    
    
    
    
    
    
    def cart_display(self):
        print("      BOOK NAME             BOOK AUTHOR             PRICE         EMAIL         QUANTITY")
        print("-----------------------------------------------------------------------------------------")
        cur.execute("select * from cart1")
        data = cur.fetchall()
        for row in data:
            rec = f"{row[1]:18s}{gap}{row[2]:20s}{gap}{row[3]:<10.2f}{gap}{row[4]:15s}{gap}{row[5]:<10d}"
            print(rec.center(100))
            
            
            
            
    def cart(self):
        print("                          Books in Cart                      ")
        self.cart_display()
        while True:
            print(" ")
            print("*******************************************************************************")
            print(" ")
            print(" 1.Remove Item From Cart     2.Go To Payment Page    3.Change Quantity   4.EXIT")
            print(" ")
            choice=int(input("Enter Your Choice :- "))
            if (choice==1):
                pass
                
            elif(choice==2):
                self.payment()
                
            elif(choice==3):
                pass
            else:
                print("******************")
                print("Enter Valid Choice")
        
        
        
        
    
    def order_book(self):
        self.Display()
        print("  ")
        print("Select Your Book From Above ")
        print("  ")
        bid = int(input("Enter Book id :- "))
        bname = input("Enter Name of a Book to Place Order \n      :- ")
        bqua = int(input("How Many Copies You want to Order \n      :- "))
        email = input("Enter your email to associate with this order: ")

        que = "select name, author, price from library1 where id = %s and name = %s"
        Values = (bid,bname)
        cur.execute(que, Values)
        data = cur.fetchone()

        if data:
            que1 = "insert into cart1 (name, author, price, quantity, email) values (%s, %s, %s, %s, %s)"
            Value1 = (data[0], data[1], data[2], bqua, email)
            cur.execute(que1, Value1)
            db.commit()
            print("Your book has been added to the cart successfully!")
        else:
            print("Book not found")
        

        while True:
            print(" ")
            print("*******************************************************************************")
            print(" ")
            print("        1.Shop More       2.Place Order     3:EXIT")
            print(" ")
            choice=int(input("Enter Your Choice :- "))
            if (choice==1):
                self.order_book()
            elif(choice==2):
                self.cart()
            elif(choice==3):
                break
            else:
                break
        
                
            
            
    def cdata(self):
        choice = 0
        while True:
            print(" ")
            print("*******************************************************************************")
            print(" ")
            print("1.Registration     2.Login    3:EXIT")
            print(" ")
            choice=int(input("Enter Your Choice :- "))
            
            if(choice==1):
                self.reg()
            elif(choice==2):
                self.login()
            elif(choice==3):
                main()
            else:
                print("******************")
                print("Enter Valid Choice")
                self.cdata()
        
                


def main():
    choice=0
    while True:
        print("*******************************************  WELCOME  *******************************************")
        print(" ")
        print("             1:ADMIN                       2:CUSTOMER                                  3:EXIT")
        print(" ")
        choice=int(input("Please Enter Your choice :- "))
        
        if (choice==1):
            a=admin()
            a.login()
        elif(choice==2):
            c=customer()
            c.cdata() 
        elif(choice==3):
            break
        else:
            break

main()
