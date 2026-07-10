#Types of Methods: instance, class, static
class Calculator:
    pi = 3.14159

    def add(self, a, b):        #instance method
        return a + b

    @classmethod
    def getPI(cls):             #class method - accesses class attr
        return cls.pi

    @staticmethod
    def isPositive(n):          #static method - no self/cls
        return n > 0

calc = Calculator()
print(calc.add(3, 5))
print(Calculator.getPI())
print(Calculator.isPositive(-4))
print(Calculator.isPositive(10))
