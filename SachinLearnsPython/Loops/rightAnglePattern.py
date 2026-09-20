#Print a right angle triangle of stars using loop
rows = int(input("Rows: "))

for i in range(1, rows + 1):
    print("*" * i)

#another
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()