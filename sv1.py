a=100                #a is an global variable
def add():
    b=200             #b is a local variable
    c=a+b
    print("sum  :",c)
add()
print("value of A",a)
 