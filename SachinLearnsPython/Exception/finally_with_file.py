# finally_with_file.py

file = None

try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    if file:
        file.close()
        print("File closed.")