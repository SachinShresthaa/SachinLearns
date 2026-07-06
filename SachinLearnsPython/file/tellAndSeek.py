with open("data.txt","w",encoding="utf-8") as f:
    f.write("ABCDEFGHIJ")

with open("data.txt","r",encoding="utf-8") as f:
    print(f.tell())
    print(f.read())
    print(f.tell())

    f.seek(0)
    print(f.read(3))

    f.seek(7)
    print(f.read())