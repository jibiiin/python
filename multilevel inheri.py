class first:
    def one(self):
        print("It is a first class ")

class second(first):
    def two(self):        
        print("it is the second class")

class third(second):
    def three(self):
        print("it is the third class")

x=third()
x.one()
x.two()
x.three()
