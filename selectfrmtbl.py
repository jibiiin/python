import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="mysql")
cur=conn.cursor()
name=input("Enter a name :")
if conn:
    cur.execute("select *from jiji where name='%s'"%name)
    result=cur.fetchall()
    for a in result:
        print("name :",a[0])
        print("mark1 :",a[1])
        print("mark2 :",a[2])
else:
    print("connection failed")    