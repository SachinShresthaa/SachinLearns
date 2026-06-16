# Write a function is_palindrome(s) that returns True if a string reads the same forwards and backwards.

def is_palindrome(s):
    return s == s[::-1]

name = "bob"
print(is_palindrome(name))
