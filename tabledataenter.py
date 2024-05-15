import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="mysqll")
cur=conn.cursor()
name=input("enter a name")
mark1=input("enter the mark1")
mark2=input("enter the mark2")
if conn:
    cur.execute("insert into shadow value('%s',%s,%s)"%(name,mark1,mark2))
    conn.commit()
    print(cur.execute,"Insert data created success")
else:
    print("connection failed")    