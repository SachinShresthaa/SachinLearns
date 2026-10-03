#Print all Armstrong numbers between 1 and 1000. Each digit raised to the number of digits sums to the number itself
for n in range(1, 1001):
    digits = len(str(n))
    total = 0
    temp = n
    while temp > 0:
        total += (temp % 10) ** digits
        temp //= 10
    if total == n:
        print(n, end=" ")
