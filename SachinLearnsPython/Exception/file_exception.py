# file_exception.py

try:
    file = open("student.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found.")

finally:
    print("Closing program.")