#Print all strong numbers between 1 and 100000. A strong number equals the sum of the factorials of its digits
for n in range(1, 100001):
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        fact = 1
        for i in range(2, digit + 1):
            fact *= i
        total += fact
        temp //= 10
    if total == n:
        print(n, end=" ")
