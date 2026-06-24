#Encapsulation - hiding data with private attributes
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance    #private (name mangled)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrawn {amount}. Balance: {self.__balance}")

    def getBalance(self):           #getter - controlled access
        return self.__balance

acc = BankAccount("Sachin", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.getBalance())

#acc.__balance = 99999  #this won't work as expected
