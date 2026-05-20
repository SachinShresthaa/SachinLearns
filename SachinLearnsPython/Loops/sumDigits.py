#Take an integer input. Sum all the sigit between it
n = int(input("Enter a number."))
total = 0
for i in range(1,n+1):
    total+=i

print("Sum of all numbers =", total)