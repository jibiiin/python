address={"name1":"A","name2" :"B","name3":"C"}
select=int(input("select a number(1 Add,2 Select, 3 edit,4 delete)"))
if select==1:
    n=input("enter a name :")
    address["name4"]=n
    print(address)
elif select==2:
    n=input("enter a selected name of id:")
    print(address[n])
elif select==3:
    n=input("enter a name of id:")
    m=input("replaced name ")
    address[n]=m
    print(address)
else:
    n=input("enter a name of id:")
    del address[n]
    print(address)



