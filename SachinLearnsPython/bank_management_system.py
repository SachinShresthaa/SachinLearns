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

    def get_account_number(self):
        return self.__account_number
    def check_balance(self):
        print(f"Current Balance: ${self.__balance:.2f}")
    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.__balance += amount

        print(f"${amount:.2f} deposited successfully.")

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self.__balance:
            raise ValueError("Insufficient balance.")

        self.__balance -= amount

        print(f"${amount:.2f} withdrawn successfully.")

    def display_info(self):

        print(f"""
------------------------------
Account Number: {self.__account_number}
Name: {self.name}
Age: {self.age}
Balance: ${self.__balance:.2f}
------------------------------
""")
    def to_dict(self):

        return {
            "account_number": self.__account_number,
            "name": self.name,
            "age": self.age,
            "balance": self.__balance
        }

    @classmethod
    def get_account_count(cls):
        return cls.account_count

    # Static Method
    @staticmethod
    def is_valid_age(age):
        return age >= 18

    class BankManagementSystem:

     def __init__(self):

        self.accounts = []

        self.file_name = "accounts.json"