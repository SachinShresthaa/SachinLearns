scores = [85, 42, 91, 67, 55, 91, 78]

# sort - ascending (modifies original)
scores.sort()
print(scores)               # [42, 55, 67, 78, 85, 91, 91]

# sort descending
scores.sort(reverse=True)
print(scores)               # [91, 91, 85, 78, 67, 55, 42]

# sorted() - returns new list, original unchanged
original = [5, 3, 8, 1]
new_sorted = sorted(original)
print(original)             # [5, 3, 8, 1] - unchanged
print(new_sorted)           # [1, 3, 5, 8]

# reverse - reverses in place
scores.reverse()
print(scores)

# index - find position of a value
print(scores.index(85))     # position of 85

# count - how many times a value appears
print(scores.count(91))     # 2

# copy - creates a shallow copy
backup = scores.copy()
backup.append(100)
print(scores)               # original unchanged
print(backup)

# clear - empties the list
temp = [1, 2, 3]
temp.clear()
print(temp)                 # []

# list to string
words = ["learn", "python", "today"]
sentence = " ".join(words)
print(sentence)             # learn python today

# string to list
csv_row = "name,age,score"
fields = csv_row.split(",")
print(fields)               # ['name', 'age', 'score']
