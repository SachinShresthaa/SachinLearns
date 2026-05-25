name = input("Enter Student Name: ")
marks = float(input("Enter Marks: "))

if marks >= 80:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Name:", name)
print("Grade:", grade)