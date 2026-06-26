#zip(), enumerate(), sorted(), any(), all()
names  = ["Sachin", "Hero", "Alice", "Bob"]
scores = [88, 95, 72, 60]

#zip - pair two lists together
paired = list(zip(names, scores))
print(paired)

for name, score in zip(names, scores):
    print(f"{name}: {score}")

#enumerate - index + value
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

#sorted with key
top = sorted(paired, key=lambda x: x[1], reverse=True)
print("Ranked:", top)

#any / all
print(any(s >= 90 for s in scores))    #True if at least one
print(all(s >= 50 for s in scores))    #True if all pass
