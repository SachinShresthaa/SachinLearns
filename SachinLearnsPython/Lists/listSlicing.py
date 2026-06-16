# List slicing — accessing elements using [start:stop:step]

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(nums[2:6])       # index 2 to 5
print(nums[:4])        # first 4 elements
print(nums[5:])        # from index 5 to end
print(nums[::2])       # every 2nd element
print(nums[1::2])      # every 2nd element starting at index 1
print(nums[::-1])      # reversed
print(nums[::-2])      # reversed, every 2nd element
print(nums[8:2:-1])    # from index 8 down to index 3
