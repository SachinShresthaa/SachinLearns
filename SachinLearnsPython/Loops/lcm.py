#Find the LCM of two positive numbers by checking multiples of the larger one
a = int(input("First number: "))
b = int(input("Second number: "))

if a <= 0 or b <= 0:
    print("Both numbers must be positive")
else:
    larger = max(a, b)
    multiple = larger
    while multiple % a != 0 or multiple % b != 0:
        multiple += larger
    print("LCM:", multiple)
