#Convert a non-negative decimal number to binary using a while loop. No bin()
n = int(input("Enter a number: "))

if n < 0:
    print("Please enter a non-negative number")
elif n == 0:
    print("Binary: 0")
else:
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    print("Binary:", binary)
