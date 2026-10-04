#Print the Collatz sequence for a positive number: halve if even, 3n + 1 if odd, until it reaches 1
n = int(input("Enter a positive number: "))

if n <= 0:
    print("Number must be positive")
else:
    steps = 0
    print(n, end=" ")
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
        print(n, end=" ")
    print()
    print("Steps:", steps)
