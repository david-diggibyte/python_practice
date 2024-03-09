# class and object

class Employee(): # class created
    company = "Diggibyte Technology"
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
    def display(self):
        print(f"{self.name} working at {self.company},domain is {self.department} and salary is {self.salary}.")


david = Employee("david","Data Engineer",10000) # object created
david.display()

k7 = Employee("k7","Data Engineer",10000)
k7.display()

dhinakaran = Employee("dhinakaran","Data Engineer",10000)
dhinakaran.display()