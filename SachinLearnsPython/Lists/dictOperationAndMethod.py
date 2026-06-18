catalog = {"apple":1.5,"mango":2.0,"banana":0.8}

#Dictonary comprehension(pythonic!)
expensive = {k:v for k,v in catalog.items() if v>1.0}

#merge two dicts(python 3.9+)
extras = {"grape":3.0, "lime":1.2}
catalog.update(extras)

#count word frequency(Classic NLP!)
text = "the cat sat on the mat the cat"
freq={}
for word in text.split():
    freq[word] = freq.get(word,0)+1

print(freq)