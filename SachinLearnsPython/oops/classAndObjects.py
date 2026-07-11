#Class and Objects
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

#creating objects
dog1 = Dog("Rex", "Labrador")
dog2 = Dog("Buddy", "Poodle")

print(dog1.name)
print(dog2.breed)
dog1.bark()
dog2.bark()
