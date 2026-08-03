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

class Order:
    total_sales=0
    def __init__(self,customer,food,qty):
        self.customer=customer
        self.food=food
        self.qty=qty
        self.total=food.get_price()*qty
        Order.total_sales+=self.total
    def to_dict(self):
        return {"customer":self.customer.name,"food":self.food.name,"qty":self.qty,"total":self.total}
    def display(self):
        print(f"{self.customer.name} | {self.food.name} | Qty:{self.qty} | Total: Rs.{self.total}")