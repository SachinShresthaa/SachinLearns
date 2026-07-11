#Inheritance - child class inherits from parent
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Cat(Animal):
    def speak(self):             #method overriding
        print(f"{self.name} says: Meow!")

class Parrot(Animal):
    def speak(self):
        print(f"{self.name} says: Hello!")

    def fly(self):               #new method in child
        print(f"{self.name} is flying")

a = Animal("Generic Animal")
c = Cat("Whiskers")
p = Parrot("Polly")

a.speak()
c.speak()
p.speak()
p.fly()

print(isinstance(c, Animal))   #True - Cat is an Animal
