import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="mysqll")
cur=conn.cursor()
if conn:
    cur.execute("select *from shadow")
    result=cur.fetchall()
    for a in result:
        print("name :",a[0])
        print("malayalam :",a[1])
        print("math :",a[2])
       
   

