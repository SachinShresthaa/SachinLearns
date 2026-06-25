#Generator expressions - lazy version of list comprehension
import sys

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#list comprehension - all values in memory
squares_list = [x**2 for x in nums]

#generator expression - lazy, one at a time
squares_gen = (x**2 for x in nums)

print(squares_list)
print(squares_gen)            #generator object
print(next(squares_gen))      #1
print(next(squares_gen))      #4

#memory comparison
big_list = [x**2 for x in range(100000)]
big_gen  = (x**2 for x in range(100000))

print(f"List size: {sys.getsizeof(big_list)} bytes")
print(f"Generator size: {sys.getsizeof(big_gen)} bytes")
