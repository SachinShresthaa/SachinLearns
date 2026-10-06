#Print all neon numbers between 0 and 10000. A neon number equals the sum of the digits of its square
for n in range(0, 10001):
    square = n * n
    digit_sum = 0
    while square > 0:
        digit_sum += square % 10
        square //= 10
    if digit_sum == n:
        print(n, end=" ")
