# 2D list = list of lists (like a table/grid)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# access element [row][column]
print(matrix[0][0])     # 1  (row 0, col 0)
print(matrix[1][2])     # 6  (row 1, col 2)
print(matrix[2][-1])    # 9  (last in last row)

# print all rows
for row in matrix:
    print(row)

# print each element
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

# modify an element
matrix[1][1] = 99
print(matrix)

# number of rows and columns
print("Rows:", len(matrix))
print("Cols:", len(matrix[0]))

# dataset example - each row is a student [name, age, score]
students = [
    ["Sachin", 20, 88],
    ["Alice",  22, 95],
    ["Bob",    21, 73]
]

for student in students:
    name, age, score = student      # unpacking
    print(f"{name} | Age: {age} | Score: {score}")

# find student with highest score
top = max(students, key=lambda s: s[2])
print("Top student:", top[0], "with score", top[2])
