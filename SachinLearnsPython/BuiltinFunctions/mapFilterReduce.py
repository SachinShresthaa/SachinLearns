#map(), filter(), reduce() - higher order functions
from functools import reduce

scores = [45, 88, 72, 95, 60, 33, 81]

#map - apply function to every element
doubled = list(map(lambda x: x * 2, scores))
print("Doubled:", doubled)

grades = list(map(lambda s: "Pass" if s >= 50 else "Fail", scores))
print("Grades:", grades)

#filter - keep elements that match condition
passing = list(filter(lambda x: x >= 50, scores))
print("Passing:", passing)

high_scores = list(filter(lambda x: x >= 80, scores))
print("High scores:", high_scores)

#reduce - collapse list to single value
total = reduce(lambda a, b: a + b, scores)
print("Total:", total)

maximum = reduce(lambda a, b: a if a > b else b, scores)
print("Max:", maximum)
