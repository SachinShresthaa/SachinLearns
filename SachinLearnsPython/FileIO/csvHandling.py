#Reading and writing CSV files
import csv
import os

students = [
    ["Name", "Age", "Score"],
    ["Sachin", 22, 88],
    ["Hero", 21, 95],
    ["Alice", 23, 76]
]

#write CSV
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)

#read CSV
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#read as dict
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} scored {row['Score']}")

os.remove("students.csv")   #cleanup
