import json
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class BankAccount(Person):

    account_count = 0

    def __init__(self, account_number, name, age, balance=0):

        super().__init__(name, age)

        self.__account_number = account_number
        self.__balance = balance

        BankAccount.account_count += 1