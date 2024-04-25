def data(a,b):
    global c
    global d
    global e
    global f
    c=a+b
    d=a-b
    e=a*b
    f=a//b
def sum():
    print("sum  :",c)
def sub():
    print("sub   :",d) 
def mul():
    print("mul   :",e)            
def div():
    print("div  :",f)    
a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
data(a,b)
sum()
sub()
mul()
div()

