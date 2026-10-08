#Print all spy numbers between 1 and 1500. A spy number has equal sum and product of its digits
for n in range(1, 1501):
    digit_sum = 0
    digit_product = 1
    temp = n
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        digit_product *= digit
        temp //= 10
    if digit_sum == digit_product:
        print(n, end=" ")
