try:
    print("remainder: name,mailid,password")
    name=input("enter your account name")
    mailid=input("enter mailid")
    password=input("enter the password")
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Go@13082003",database="user")
    mycursor=mydb.cursor()
    query="insert into details values(%s,%s,%s)"

    record=(name,mailid,password)
    mycursor.execute(query,record)
    mydb.commit()
    print("added")
    choice=input("do you want to add someting else? (yes/no)")
    if choice.upper()=="YES":
        a=1
    else:
        print("thank you")
        a="done"
except:
    print("check out..")
