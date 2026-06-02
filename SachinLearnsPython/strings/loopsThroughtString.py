#for loop
text = "sachin"
for ch in text:
    print(ch,end="")
#Enumerate
for i, ch in enumerate(text):
    print(f"{i}:{ch}",end="")
#cooprehension
vowels = [c for c in text if c in "aeiou"]
print(vowels)