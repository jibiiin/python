name=["A","B","C"]
select=int(input("select a number(1 Add, 2 Select, 3 Edit, 4 Delete)"))
if select==1:
    n=input("enter a name:")
    name.append(n)
    print(name)
elif select==2:
    n=input("enter a selected name:")
    data=name.index(n)
    print("Your selected name :",name[data])
elif select==3:
    n=input("enter a name")
    m=input("replaced name")
    data=name.index(n)
    name[data]=m
    print(name)
else:
    n=input("enter a name")
    data=name.index(n)
    del name[data]
    print(name)

        