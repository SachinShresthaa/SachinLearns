text = "MachineLearning"

# basic slicing [start:stop]
print(text[0:7])        # Machine
print(text[7:])         # Learning
print(text[:7])         # Machine

# negative indexing
print(text[-8:])        # Learning
print(text[-8:-4])      # Lear
print(text[-1])         # g (last character)

# step slicing [start:stop:step]
print(text[::2])        # every 2nd character
print(text[::3])        # every 3rd character
print(text[::-1])       # reverse the string
print(text[1::2])       # every 2nd char starting from index 1

# extracting specific parts
sentence = "the quick brown fox"
words = sentence.split()
print(words[1:3])       # ['quick', 'brown']

# reversing words in a sentence
reversed_words = " ".join(sentence.split()[::-1])
print(reversed_words)   # fox brown quick the

# slicing to check palindrome
word = "racecar"
print(word == word[::-1])   # True

word2 = "hello"
print(word2 == word2[::-1]) # False
