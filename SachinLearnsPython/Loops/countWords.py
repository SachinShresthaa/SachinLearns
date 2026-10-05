#Count the words in a sentence without using split()
sentence = input("Enter sentence: ")
count = 0
in_word = False

for char in sentence:
    if char == " ":
        in_word = False
    elif not in_word:
        in_word = True
        count += 1

print("Words:", count)
