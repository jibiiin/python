import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="mysqll")
cur=conn.cursor()
if conn:
    cur.execute("create table shadow(name char(20),eng int,math int)")
    print("Table created success")
else:
    print("connection failed")    