# encapsulation

class Company():
    def __init__(self,company,name,salary):
        self.__company = company                # private (__)
        self._name = name                       # protected (_)
        self.salary = salary                     # private
    def show(self):
        print(f"{self._name} working {self.__company} and salary is {self.salary}")

david = Company("david","diggibyte",10000)
david.show()
david.__company = "ddddd"