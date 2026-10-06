#Print Pascal's triangle for N rows. Each number is the sum of the two above it
rows = int(input("Rows: "))
row = [1]

for i in range(rows):
    print(" " * (rows - i - 1) + " ".join(str(x) for x in row))
    next_row = [1]
    for j in range(len(row) - 1):
        next_row.append(row[j] + row[j + 1])
    next_row.append(1)
    row = next_row
