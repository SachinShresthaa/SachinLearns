#Find the smallest and largest number in a list without min() or max()
nums = [12, 45, 7, 89, 56, 34]
smallest = nums[0]
largest = nums[0]

for n in nums:
    if n < smallest:
        smallest = n
    if n > largest:
        largest = n

print("Smallest:", smallest)
print("Largest:", largest)
