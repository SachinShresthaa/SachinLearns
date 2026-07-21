# with_open.py

try:
    with open("student.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")