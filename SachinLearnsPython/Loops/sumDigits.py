#Take an integer input. Sum all the numbers from 1 to it
n = int(input("Enter a number."))
total = 0
for i in range(1, n + 1):
    total += i

print("Sum of all numbers =", total)