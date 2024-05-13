import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="mysql")
cur=conn.cursor()
name=input("enter table name")
name1=input("enter fieldname1")
name2=input("enter fieldname2")
name3=input("enter fieldname3")

if conn:
    cur.execute("create table %s(%s char(20),%s int,%s int)"%(name,name1,name2,name3))
    print("Table created success")
else:
    print("connection failed")    