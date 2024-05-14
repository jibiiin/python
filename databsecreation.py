import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="")
cur=conn.cursor()
name=input("enter the database name")
if conn:
    cur.execute("CREATE DATABASE %s"%(name))
    print(name, "Database created success")
else:
    print("connection failed")    