#Print all prime numbers between 1 and a user given limit using nested loops
limit = int(input("Limit: "))

for n in range(2, limit + 1):
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")
