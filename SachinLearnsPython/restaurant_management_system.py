import json

class Person:
    def __init__(self,name):
        self.name=name

class Customer(Person):
    pass

class FoodItem:
    def __init__(self,item_id,name,price):
        self.item_id=item_id
        self.name=name
        self.__price=price
    def get_price(self):
        return self.__price
    def display(self):
        print(f"{self.item_id}. {self.name:<15} Rs.{self.__price}")