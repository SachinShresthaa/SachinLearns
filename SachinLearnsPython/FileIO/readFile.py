#Reading files in Python
import os

#create a sample file first
with open("sample.txt", "w") as f:
    f.write("Hello Python\nLine 2\nLine 3\n")

#read entire file
with open("sample.txt", "r") as f:
    content = f.read()
    print("Full content:")
    print(content)

#read line by line
with open("sample.txt", "r") as f:
    print("Line by line:")
    for line in f:
        print(line.strip())

#read into list
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(f"Total lines: {len(lines)}")

os.remove("sample.txt")   #cleanup
