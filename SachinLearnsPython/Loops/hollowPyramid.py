#Print a hollow pyramid of stars: only the edges and the base are filled
rows = int(input("Rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2 or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()
