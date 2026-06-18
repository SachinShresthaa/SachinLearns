grades = {"Sach":90,"HAAAA":75,"Ram":88,"DAN":64}

#1. Iterate keys
for name in grades:
    print(name, end="")

#2. Iterate values - compute average
avg = sum(grades.values())/len(grades)
print(f"Average: {avg:.1f}")

#3. Iterate items - filter & display
print("Passed students:")
for name, score in grades.items():
    if score>=70:
        print(f"{name}:{score}")

#4. Sort by score desending
ranked = sorted(grades.items(),key=lambda x:x[1], reverse= True)
print("Ranking:", ranked)