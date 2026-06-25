#Set and Dictionary Comprehensions
scores = {"Sachin": 88, "Hero": 95, "Alice": 72, "Bob": 60}

#dict comprehension - transform values
doubled = {name: score * 2 for name, score in scores.items()}
print(doubled)

#dict comprehension with filter - only passing students
passing = {name: score for name, score in scores.items() if score >= 75}
print(passing)

#set comprehension - unique values
nums = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {x**2 for x in nums}
print(unique_squares)

#swap keys and values
inverted = {score: name for name, score in scores.items()}
print(inverted)
