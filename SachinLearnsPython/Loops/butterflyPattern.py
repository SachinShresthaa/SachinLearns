#Print a butterfly pattern of stars with N rows in each half
n = int(input("N: "))

# Top half
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# Bottom half
for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
