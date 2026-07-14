#Multiple Inheritance and MRO (Method Resolution Order)
class Flyable:
    def fly(self):
        print(f"{self.name} is flying")

class Swimmable:
    def swim(self):
        print(f"{self.name} is swimming")

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name

    def quack(self):
        print(f"{self.name} says: Quack!")

d = Duck("Donald")
d.fly()
d.swim()
d.quack()

#MRO - order Python searches for methods
print(Duck.__mro__)
