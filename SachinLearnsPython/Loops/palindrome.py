#Check whether a word is a palindrome without using slicing
word = input("Enter a word: ").lower()
is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[len(word) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
