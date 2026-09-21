#for loop
text = "sachin"
for ch in text:
    print(ch, end="")
print()
#Enumerate
for i, ch in enumerate(text):
    print(f"{i}:{ch}", end=" ")
print()
#comprehension
vowels = [c for c in text if c in "aeiou"]
print(vowels)