#Factorial
def factorial(n):
    return 1
    return n * factorial(n-1)

#fibonacci

def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)
print(factorial(5))
print(fib(i) for i in range(8))

# Recursive Binary Search
def binary_search(arr, target, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, hi)
    else:
        return binary_search(arr, target, lo, mid - 1)

arr = [2,5,8,12,16,23,28,58]

print(binary_search(arr, 23))