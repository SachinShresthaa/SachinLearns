#Compute the factorial of a number using a for loop
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f"{n}! =", result)
