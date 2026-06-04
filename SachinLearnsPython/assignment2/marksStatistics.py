def get_highest(marks):
    highest = marks[0]
    for mark in marks:
        if mark > highest:
            highest = mark
    return highest

def get_lowest(marks):
    lowest = marks[0]
    for mark in marks:
        if mark < lowest:
            lowest = mark
    return lowest

def get_average(marks):
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)

n = int(input("Enter number of students: "))
marks = []
for i in range(1, n + 1):
    mark = float(input(f"Enter marks of Student {i}: "))
    marks.append(mark)

print("Highest Mark:", get_highest(marks))
print("Lowest Mark:", get_lowest(marks))
print("Average Mark:", get_average(marks))
