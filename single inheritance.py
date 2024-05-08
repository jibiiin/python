class first:
    def one(self):
        print("It is a first class ")

class second(first):
    def two(self):        
        print("it is the second class")
x=second()
x.one()
x.two()

