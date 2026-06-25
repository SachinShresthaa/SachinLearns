#Nested List Comprehension
#flatten a 2D matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)

#transpose a matrix
transposed = [[row[i] for row in matrix] for i in range(3)]
for row in transposed:
    print(row)

#multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in table:
    print(row)

#filter nested: only even numbers from 2D list
evens = [num for row in matrix for num in row if num % 2 == 0]
print(evens)
