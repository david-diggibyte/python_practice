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
