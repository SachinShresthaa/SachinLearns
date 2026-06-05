# Create a function that accepts a list of marks. 
# ● Use loops to calculate grades: 
# ○ A → 80 and above 
# ○ B → 60–79 
# ○ C → 40–59 
# ○ F → Below 40 
# ● Use a lambda function to sort marks in descending order. 
# ● Display: 
# ○ Sorted marks 
# ○ Grade distribution 
# ○ Number of passed students
def process_marks(marks):
    sorted_marks = sorted(marks, key=lambda x: x, reverse=True)

    grades = {"A": 0, "B": 0, "C": 0, "F": 0}
    passed = 0

    for mark in marks:
        if mark >= 80:
            grades["A"] += 1
        elif mark >= 60:
            grades["B"] += 1
        elif mark >= 40:
            grades["C"] += 1
        else:
            grades["F"] += 1

        if mark >= 40:
            passed += 1

    print("Sorted Marks (Descending):", sorted_marks)
    print("Grade Distribution:")
    for grade, count in grades.items():
        print(f"  Grade {grade}: {count} student(s)")
    print("Number of Passed Students:", passed)

n = int(input("Enter number of students: "))
marks = []
for i in range(1, n + 1):
    mark = float(input(f"Enter marks of Student {i}: "))
    marks.append(mark)

process_marks(marks)
