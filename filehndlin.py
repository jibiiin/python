file=open("data.txt","w")
a=int(input("enter first number"))
b=int(input("enter second number"))
c=a+b
d=a-b
e=a*b
f=a//b
file.write("sum:"+str(c)+"\nsub:"+str(d)+"\nmul:"+str(e)+"\ndiv:"+str(f))
print("writing succesfully")           
