# encapsulation

class Company():
    def __init__(self,company,name,salary):
        self.__company = company             # private (__)
        self._name = name                       # protected (_)
        self.salary = salary                     # private
    def show(self):
        print(f"{self._name} working {self.__company} and salary is {self.salary}")

david = Company("diggibyte","david",10000)
david.show()
david.__company ="Google"   # did not change the company name
david._name = "mani"
david.show()


# Another example

class Collage():
    def __init__(self,principle,hod,teacher):
        self.__collage_name = "PSG"       # private
        self.__principle = principle      # private
        self._hod = hod                    # protected
        self.teacher = teacher
    def display(self):
        return f"The name of the college is {self.__collage_name}.The principal's name is {self.__principle},{self._hod} is the computer science HOD and tutor name is {self.teacher}."

robert = Collage("selavm","robert","youraj")
print(robert.display())

robert.__collage_name = "Hindusthan"   # didn't change the collage name
robert.__principle = "fffffffff"       # even didn't change the principle name
robert._hod = "mariya"
print(robert.display())