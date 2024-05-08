class bank:
    def data(self,a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
        self.g=g
    def customer(self):
        self.a=input("enter customer name   :")
        self.b=int(input("enter account number   :"))
        print("customer details obtained")         
     
    def banking(self):
        self.c=int(input("enter the loan amount :"))
        self.d=int(input("enter intrest amount  :"))
        self.e=int(input("number of years  :"))
        print("details about banking")

    def intrest(self):
        self.f=self.c*self.d*self.e//100
        print("intrest amount",self.f)    

    def emi(self):
        self.g=(self.c+self.f)//(self.e*12)
        print("emi   :",self.g)

x=bank()
x.customer()
x.banking()
x.intrest()
x.emi()

