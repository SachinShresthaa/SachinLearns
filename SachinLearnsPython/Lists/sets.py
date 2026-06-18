#creting sets
tags={"python","ml","python","ai","ml"}
print(tags)
nums = set([1,2,2,3,3,3,4])
print(nums)

#o(1) membership test
vocab = set(["hello","world","python"])
print("python" in vocab)
print("jave" in vocab)

#set operations
a = {1,2,3,4,5}
b={4,5,6,7,8}
print(a&b) #intersection
print(a|b) #union
print(a-b) #difference