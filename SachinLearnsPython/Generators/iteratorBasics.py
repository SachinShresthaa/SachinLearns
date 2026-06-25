#Iterators - __iter__ and __next__
class CountUp:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):     #makes object iterable
        return self

    def __next__(self):     #returns next value
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

counter = CountUp(1, 5)
for num in counter:
    print(num)

#built-in iter() and next()
nums = iter([10, 20, 30])
print(next(nums))
print(next(nums))
print(next(nums))
