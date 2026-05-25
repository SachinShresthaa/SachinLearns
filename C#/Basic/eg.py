class Student:
    
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating Object
s1 = Student("Sachin", 20)

# Calling Method
s1.display()