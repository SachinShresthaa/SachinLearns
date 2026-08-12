#LIFECYCLE
f = open("notes.txt","w")
f.write("Hello,Python!")
f.close()

with open("notes.txt","r") as f:
    content = f.read()
    print(content)