#Find the longest word in a sentence without using max()
sentence = input("Enter sentence: ")
longest = ""

for word in sentence.split():
    if len(word) > len(longest):
        longest = word

if longest == "":
    print("No words entered")
else:
    print("Longest word:", longest)
