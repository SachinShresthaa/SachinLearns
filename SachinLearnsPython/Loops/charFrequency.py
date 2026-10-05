#Count how many times each character appears in a user entered word
word = input("Enter a word: ")
freq = {}

for char in word:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for char, count in freq.items():
    print(f"{char}: {count}")
