#Abstraction - hide complexity using abstract classes
from abc import ABC, abstractmethod

class Vehicle(ABC):             #abstract base class
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def fuelType(self):         #must be implemented by subclass
        pass

    @abstractmethod
    def maxSpeed(self):
        pass

    def info(self):             #concrete method - shared behavior
        print(f"{self.brand} | Fuel: {self.fuelType()} | Max: {self.maxSpeed()} km/h")

class Car(Vehicle):
    def fuelType(self):
        return "Petrol"
    def maxSpeed(self):
        return 200

class ElectricBike(Vehicle):
    def fuelType(self):
        return "Electric"
    def maxSpeed(self):
        return 120

c = Car("Toyota")
e = ElectricBike("Yadea")
c.info()
e.info()

#v = Vehicle("Test")  #TypeError: can't instantiate abstract class
