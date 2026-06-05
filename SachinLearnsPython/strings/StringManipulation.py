text = "Sachin Shrestha"

# 1 Clean and m=normalize

clean = text.strip().lower()
print(clean)    

# 2 Replace and split
replaced = clean.replace(",", "").split()
print(replaced) 

#3.Reversed
reversed_text = clean[::-1]
print(reversed_text)
