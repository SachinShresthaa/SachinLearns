# Given a list of names, normalize each name (strip whitespace, title case) and print the cleaned list.

names = ["  sachin hero  ", "YO YO Honey", " Love Lace ", "COMPUTER   "]

cleaned = [name.strip().title() for name in names]

print(cleaned)
