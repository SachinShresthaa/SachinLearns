#Check whether a number is prime using a loop
n = int(input("Enter a number: "))

if n < 2:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")