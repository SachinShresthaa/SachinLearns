#try / except / finally
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")

except ValueError:
    print("Error: Please enter a valid integer!")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

finally:
    print("This always runs - cleanup here")
