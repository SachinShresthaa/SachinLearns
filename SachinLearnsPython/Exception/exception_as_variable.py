# exception_as_variable.py

try:
    num = int(input("Enter number: "))
    print(100 / num)

except Exception as error:
    print("Error:", error)