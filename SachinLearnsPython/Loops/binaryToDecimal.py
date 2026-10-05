#Convert a binary string to decimal using a for loop. No int(x, 2)
binary = input("Enter a binary number: ")
decimal = 0
valid = binary != ""

for bit in binary:
    if bit not in "01":
        valid = False
        break
    decimal = decimal * 2 + int(bit)

if valid:
    print("Decimal:", decimal)
else:
    print("Invalid binary number")
