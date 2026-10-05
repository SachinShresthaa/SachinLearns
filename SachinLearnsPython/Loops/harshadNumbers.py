#Print all Harshad numbers between 1 and 100. A Harshad number is divisible by the sum of its digits
for n in range(1, 101):
    digit_sum = 0
    temp = n
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    if n % digit_sum == 0:
        print(n, end=" ")
