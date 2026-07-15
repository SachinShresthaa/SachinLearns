# zero_division_error.py

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(result)

except ZeroDivisionError:
    print("You cannot divide by zero.")