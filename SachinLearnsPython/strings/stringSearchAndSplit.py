text = "learn python, learn AI, learn ML"

# count occurrences
print(text.count("learn"))              # 3
print(text.count("learn", 10))         # count from index 10 onwards

# find vs index
print(text.find("AI"))                 # returns index or -1 if not found
print(text.find("Java"))               # -1 (not found, no error)
# print(text.index("Java"))            # would raise ValueError

# rfind - search from the right
print(text.rfind("learn"))             # index of last "learn"

# partition - splits into 3 parts at first match
before, sep, after = text.partition(",")
print(before)   # learn python
print(sep)      # ,
print(after)    # learn AI, learn ML

# rpartition - splits at last match
before, sep, after = text.rpartition(",")
print(before)   # learn python, learn AI
print(after)    # learn ML

# splitlines - split by newlines
multiline = "line one\nline two\nline three"
print(multiline.splitlines())

# swapcase - swap upper and lower
mixed = "SaCHiN sHRESTHA"
print(mixed.swapcase())         # sAchIn Shrestha

# casefold - aggressive lowercase (good for comparisons)
print("Straße".casefold())      # strasse

# removeprefix / removesuffix (Python 3.9+)
filename = "report_final.csv"
print(filename.removeprefix("report_"))    # final.csv
print(filename.removesuffix(".csv"))       # report_final
