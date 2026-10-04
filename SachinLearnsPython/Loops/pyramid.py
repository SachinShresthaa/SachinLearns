#Print a full pyramid of stars centred with spaces
rows = int(input("Rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
