#Capitalize the first letter of every word in a sentence without using title() or capitalize()
sentence = input("Enter sentence: ")
result = ""
prev = " "

for char in sentence:
    if prev == " " and "a" <= char <= "z":
        result += chr(ord(char) - 32)
    else:
        result += char
    prev = char

print(result)
