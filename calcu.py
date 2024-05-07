class Calculation:
    def data(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        c=self.a+self.b
        print("sum  :",c)
    def multiplication(self):
        d=self.a*self.b
        print("multiplication :",d)  
    def subtraction(self):
        e=self.a-self.b
        print("subtraction :",e)     
    def division(self):
        f=self.a//self.b
        print("division  :",f)          
x=Calculation()
x.data(10,10)
x.sum() 
x.multiplication()    
x.subtraction()       
x.division()