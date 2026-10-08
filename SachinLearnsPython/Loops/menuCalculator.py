#Simple calculator that keeps running in a while loop until the user chooses to quit
while True:
    op = input("Operation (+, -, *, /) or q to quit: ")
    if op == "q":
        print("Goodbye")
        break
    if op not in ("+", "-", "*", "/"):
        print("Invalid operation")
        continue

    a = float(input("First number: "))
    b = float(input("Second number: "))

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif b == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", a / b)
