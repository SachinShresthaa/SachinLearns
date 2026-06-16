#WAP that takes a sentence and counts the number of vowels and consonants

sentence = input("Enter a sentence: ")
vowels = 0
consonants = 0

for char in sentence.lower():
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
