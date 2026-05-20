#Compute base^exp using only multiplication in a for loop. No ** or pow()

base = int(input("Enter the base number: "))
exp=int (input("Exponent: "))
result = 1

for _ in range(exp):
    result = result*base

print ("Result: ", result)