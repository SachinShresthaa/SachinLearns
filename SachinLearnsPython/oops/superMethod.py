#super() - calling parent class methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}, age {self.age}")

class Employee(Person):
    def __init__(self, name, age, company, salary):
        super().__init__(name, age)   #call parent __init__
        self.company = company
        self.salary = salary

    def introduce(self):
        super().introduce()           #call parent method
        print(f"I work at {self.company}, salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, age, company, salary, team_size):
        super().__init__(name, age, company, salary)
        self.team_size = team_size

    def introduce(self):
        super().introduce()
        print(f"I manage a team of {self.team_size}")

m = Manager("Sachin", 22, "TechCorp", 80000, 10)
m.introduce()
