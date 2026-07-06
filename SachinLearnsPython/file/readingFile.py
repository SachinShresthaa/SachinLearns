with open("scores.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(repr(content))

with open("scores.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    scores = [int(ln.split()[1]) for ln in lines]
    print("Avg", sum(scores)/len(scores))

