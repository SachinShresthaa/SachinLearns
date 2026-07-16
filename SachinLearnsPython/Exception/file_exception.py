# file_exception.py

try:
    file = open("student.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Closing program.")