#Find the GCD of two numbers using the Euclidean algorithm in a while loop
a = int(input("First number: "))
b = int(input("Second number: "))
a, b = abs(a), abs(b)

while b != 0:
    a, b = b, a % b

print("GCD:", a)
