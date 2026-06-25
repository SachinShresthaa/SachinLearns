#Generator functions - yield keyword
def countUp(start, end):
    current = start
    while current <= end:
        yield current         #pauses and returns value
        current += 1

#lazy - values generated one at a time
for num in countUp(1, 5):
    print(num)

#fibonacci generator
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print(list(fibonacci(8)))

#generator saves memory vs list
gen = countUp(1, 1000000)   #no memory used yet
print(next(gen))            #only one value computed
