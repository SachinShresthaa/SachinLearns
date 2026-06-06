numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# basic comprehension - square each number
squares = [n ** 2 for n in numbers]
print(squares)

# with condition - only even numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)

# with condition - odd numbers squared
odd_squares = [n ** 2 for n in numbers if n % 2 != 0]
print(odd_squares)

# transform strings
names = ["sachin", "alice", "bob"]
upper_names = [name.upper() for name in names]
print(upper_names)

# filter strings by length
long_names = [name for name in names if len(name) > 3]
print(long_names)

# nested list comprehension - multiplication table
table = [[row * col for col in range(1, 6)] for row in range(1, 6)]
for row in table:
    print(row)

# flatten a 2D list into 1D
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)

# ML use case - normalize scores between 0 and 1
raw_scores = [50, 75, 90, 40, 100]
max_score = max(raw_scores)
normalized = [round(s / max_score, 2) for s in raw_scores]
print(normalized)
