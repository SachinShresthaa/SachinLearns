def getHighest(marks):
    highest = marks[0]
    for mark in marks:
        if mark > highest:
            highest = mark
    return highest

def getLowest(marks):
    lowest = marks[0]
    for mark in marks:
        if mark < lowest:
            lowest = mark
    return lowest

def getAverage(marks):
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)

n = int(input("Enter number of students: "))
marks = []
for i in range(1, n + 1):
    mark = float(input(f"Enter marks of Student {i}: "))
    marks.append(mark)

print("Highest Mark:", getHighest(marks))
print("Lowest Mark:", getLowest(marks))
print("Average Mark:", getAverage(marks))
