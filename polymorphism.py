# Polymorphisam

print(type("david"))
print(type(555))

class Addition():
    def __init__(self,a,b,c = 0):
        self.a = a
        self.b = b
        self.c = c
    def add(self):
        return self.a + self.b + self.c

sum1 = Addition(30,50)
print(sum1.add())

sum2 = Addition(50,50,50)
print(sum2.add())

sum3 = Addition(2,2,2)
print(sum3.add())

# Method overloading another example

class Multiplication():
    total = 1
    def mul(self,*args):
       total = 1
       for i in args:
        total *=  i
       return total

mul1 = Multiplication()
print(mul1.mul(5,5))

mul2 = Multiplication()
print(mul2.mul(1,2,3,4,5))

mul3 = Multiplication()
print(mul3.mul(100,100,100))
