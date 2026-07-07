students = [{"Alice",92},{"bob",85},{"Carol",78}]
with open("results.txt","w",encoding="utf-8") as f:
    f.write("===Exam result===")
for name,score in students:
    f.write(f"{name}:{score}")

lines = [f"{n}:{s}" for n,s in students]
with open("scores.txt","r",encoding="utf-8") as f:
    f.writelines(lines)
