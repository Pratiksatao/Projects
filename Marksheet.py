#student Marksheet

name=str(input("enter your name :- "))
submark=100
pmark=int(input("enter physics marks :- "))
if(pmark >submark):
        print("Enter valid marks")
        pmark=int(input("enter physics marks :- "))

cmark=int(input("enter chemistry marks :- "))
if(cmark >submark):
    print("enter vaild marks")
    cmark=int(input("enter chemistry marks :- "))

mmark=int(input("enter maths marks :- "))
if(mmark >submark):
    print("enter vaild marks")
    mmark=int(input("enter maths marks :- "))
tmarks=submark+submark+submark

pper=(pmark/submark)*100
cper=(cmark/submark)*100
mper=(mmark/submark)*100
omarks=pmark+cmark+mmark
per=(omarks/tmarks)*100

print("                             Student name :- ",name )
print("Totle Marks :- ",tmarks)
print("Obtain Marks :- ",omarks)
print("Subjects             Total Marks         Obtain marks            Persentage")
print("==================================================================================")
print("physics             ",submark,"                  ",pmark,"               ",pper)
print("chemistry           ",submark,"                  ",cmark,"               ",cper)
print("maths               ",submark,"                  ",mmark,"               ",mper)
print("==================================================================================")
print("Total               ",tmarks,"                   ",omarks,"           ",per)