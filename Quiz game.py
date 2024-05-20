# #Mysql steps before running This Program

# 1. create database quiz;
# 2. create table ques(num int primary key auto_increment,question varchar(100),option1 varchar(50),option2 varchar(50),option3 varchar(50),option3 varchar(50),answer varchar(50),admin_id int);
# 3. create table reg (id int primary key auto_increment,a_name varchar(100),password varchar(20));
# 4. create table players(id int primary key auto_increment,p_name varchar(50),score int);
# 5. alter table ques add foreign key (admin_id) references reg (id);



import mysql.connector

db = mysql.connector.connect(host = "localhost",
                             user = "root"  ,
                             password = "Pratik1506" ,
                             database = "quiz")

cur = db.cursor()

class admin:
    def reg(self):
        Aname = input("Enter Your name :- ")
        Apassword = input("Set password :- ")
        cpassword = input("Confirm password :- ")
        if (Apassword == cpassword):
            
            query = "insert into reg(a_name,password) values (%s,%s)"
            values = (Aname,Apassword)
            cur.execute(query,values)
            
            query2 = "select id from reg where a_name = %s and password = %s"
            cur.execute(query2,(Aname,Apassword))
            data = cur.fetchone()
            for i in data:
                print("******************************************************")
                print("Your Admin id is :-  ",i,end=" ")
                print("                # provide your admin id to Players")
            db.commit()
            print("          ")
            print("\n Registration Successful")
        else:
            print("Enter valid data")

    def ques(self,id):
        while True:
            
            question = input("Write a  question :- ")
            option1 = input("Option 1 :- ")
            option2 = input("Option 2 :- ")
            option3 = input("Option 3 :- ")
            option4 = input("Option 4 :- ")
            Answer = input("Answer :- ")
            
            add = input("Add another question ? (Y/N) :- ")
            
            query = "insert into ques(question,option1,option2,option3,option4,answer,admin_id)values(%s,%s,%s,%s,%s,%s,%s)"
            values=(question,option1,option2,option3,option4,Answer,id)
            cur.execute(query,values)
            db.commit()
            if(add=="Y" or add=="y"):
                self.ques(id)
            else:
                print("***************************")
                main()
                
                
    def login(self):
        name = input("Enter Username :- ")
        password = input("Enter Password :- ")
        
        query="select * from reg where a_name = %s AND password = %s"
        cur.execute(query,(name,password))
        result = cur.fetchone()
        
        if result:
            print("login Successful!. Welcome ",name)
            id= int(input("Enter Your Admin id :- "))
            self.ques(id)
        
        else:
            print("Invalid Username or Password ! Try again")
            self.login()


    def menu(self):
        while True:
            print("=======================================")
            print(" 1.Register ")
            print(" 2.Login ")
            print("=======================================")
            choice=int(input("Enter Your choice :-"))
            print("=======================================")
            if(choice==1):
                self.reg()
            elif(choice==2):
                self.login()
            else:
                break



class players:
    def player(self):
        print ("Welcome to the quiz game ")
        
        print("Fill the details")
        name = input("Enter Your Name :-  ")
        number = int(input("Enter Your Contact number :- "))
        tname = input("Enter Your Admin Name :- ")
        tid = int(input("Admin id :-"))
        
        e=input("Thank you for details \n Please press Enter to start QUIZ ")
        
        
        query3="select question,option1,option2,option3,option4 from ques where admin_id = %s"
        values = (tid,)
        cur.execute(query3,values)
        data = cur.fetchall()
        ans_list = []
        print("===========================")
        for i in data:
            
            for o in i:
                print(o)
            print("***************************")
            ans=input("Answer :-  ")
            ans_list.append(ans)
            print("===========================")
        print(ans_list)
        query4="select answer from ques where admin_id = %s"
        cur.execute(query4,values)
        ans_data = cur.fetchall()
        correct_answers = [ans[0] for ans in ans_data]
        
        print("Correct Answers:", correct_answers)
        
        point = 0
        
        for indexi in range(len(ans_list)):
             if ans_list[indexi] == correct_answers[indexi]:
                 point += 1
                    
        print("Your Score is :- ",point)        
        
        
   

def main():
    while True:
        print("=======================================")
        print("1.Admin")
        print("2.Player")
        print("=======================================")
        c =int(input("Enter Your choice :-"))
        print("***************************************")
        if(c==1):
            a=admin()
            a.menu()

        elif(c==2):
            p=players()
            p.player() 
        else:
            break



main()