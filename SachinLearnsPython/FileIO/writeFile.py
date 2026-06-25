#Writing and appending to files
import os

#write mode - creates or overwrites
with open("notes.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")

#append mode - adds to existing file
with open("notes.txt", "a") as f:
    f.write("Appended line\n")

#write multiple lines at once
lines = ["Python\n", "is\n", "awesome\n"]
with open("notes.txt", "a") as f:
    f.writelines(lines)

#verify
with open("notes.txt", "r") as f:
    print(f.read())

os.remove("notes.txt")   #cleanup
