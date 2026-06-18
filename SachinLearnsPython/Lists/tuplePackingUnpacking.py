#packeting(implicit)
student = "sachin", 22, 92.5 #creates tuples

#unpacking
names, age, score = student
print(names, age, score)

#Extended unpacketing(*)
first, *rest = [10,20,30,40,50]
print(first, rest)

#swap variables(pythonic!)
a,b = 5,10
a,b =b,a
print(a,b)

#function returning multiple values
def min_max(lst):
    return min(lst), max(lst)

lo, hi =min_max([3,1,9,5])
print(lo,hi)