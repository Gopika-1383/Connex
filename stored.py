counter1=1
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Go@13082003",database="user")
mycursor=mydb.cursor()
try:
    name=input("enter the name")
    password=input("enter the password")
    mycursor.execute("select * from details where name='%s' and password='%s'"%(name,password))
    x=mycursor.fetchall()
    if x==[]:
        counter1=2
    else:
        print("user matched")
        print("so,here your account will be encrypted and secured")
                
except:
    print("error occured")
    counter1=0
if counter1==2 :
    print("User and password not matched")
