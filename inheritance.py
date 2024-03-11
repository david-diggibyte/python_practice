# inheritance
# single inheritance

class Dad():
    def dad(self):
        print("this is dad base class")
class Son(Dad):
    def son(self):
        print("this is son derived class ")

dad1 = Dad()
dad1.dad()

david = Son()
david.son()
david.dad()

# Multiple inheritance

class Dad():
    def dad(self):
        print("this is dad base class")
class Mom():
    def mom(self):
        print("this is mom base class")
class Son(Dad,Mom):
    def son(self):
        print("this is son derived class ")

dad1 = Dad()
dad1.dad()

mom1 = Mom()
mom1.mom()

david = Son()
david.son()
david.dad()
david.mom()


# multilevel inheritance



class Grand_father():
    def grand_father(self):
        print("this is grand_father base class")
class Mom(Grand_father):
    def mom(self):
        print("this is mom base class")
class Son(Mom):
    def son(self):
        print("this is son derived class ")

david = Son()
david.son()
david.mom()
david.grand_father()