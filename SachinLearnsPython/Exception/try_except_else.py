# try_except_else.py

try:
    num = int(input("Enter a number: "))
    result = 50 / num

except ZeroDivisionError:
    print("Division by zero is not allowed.")

else:
    print("Result:", result)