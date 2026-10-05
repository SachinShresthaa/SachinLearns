#Print an N*N multiplication grid using nested loops
n = int(input("N: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")
    print()
