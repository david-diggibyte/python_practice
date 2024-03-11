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


#  method overriding
# method overriding  is a function have same name and same parameter.

class Tutorial():
    def __init__(self,name):
        self.name = name
    def show(self):
        return f"{self.name} institute "
class course(Tutorial):
    def __init__(self,subject):
        self.subject = subject
    def show(self):
        return f"{self.subject} course "

sla = Tutorial("SLA")
print(sla.show())

python = course("python")
print(python.show())

java = course("java")
print(java.show())

# example two for overloading

class Animal():
    def animal(self):
        print("sound ")
class Dog(Animal):
    def dog(self):
        super().animal()
        print("Bark")
    def tommy(self):
        super().animal()
        print("tommy bark")

lion = Animal()
lion.animal()

dog1 = Dog()
dog1.dog()

dog2 = Dog()
dog2.tommy()

# another example

class Phone():
    def __init__(self,colour,ram):
        self.colour = colour
        self.ram = ram
    def specification(self):
        print(f"phone colour is {self.colour} and {self.ram} RAM.")
class Nokia(Phone):
    def __init__(self,colour,ram,model,storage):
       super().__init__(colour,ram)
       self.model = model
       self.storage = storage
    def specification(self):
        print(f"{self.model} phone colour is {self.colour},{self.ram} ROM and storage is {self.storage}.")

ph1 = Phone("red",6)
ph1.specification()

nokiya1 = Nokia("blue",6,"nokia",8)
nokiya1.specification()

nokiya2 = Nokia("red",12,"nokiya",128)
nokiya2.specification()