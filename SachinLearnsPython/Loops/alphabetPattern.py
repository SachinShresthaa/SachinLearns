#Print a triangle of letters: A, AB, ABC ... up to N rows
rows = int(input("Rows (1-26): "))

for i in range(1, rows + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
