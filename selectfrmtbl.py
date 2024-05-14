import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="mysql")
cur=conn.cursor()
if conn:
    cur.execute("select *from jiji")
    result=cur.fetchall()
    for a in result:
        print("Name :",a[0],a[1])
else:
    print("connection failed")    