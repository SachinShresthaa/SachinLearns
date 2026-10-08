#Print an hourglass of stars with N rows in each half
n = int(input("N: "))

# Top half
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Bottom half
for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
