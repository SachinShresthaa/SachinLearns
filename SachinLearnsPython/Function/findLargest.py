def largest(nums):

    big = nums[0]

    for n in nums:
        if n > big:
            big = n

    return big

numbers = [4,9,2,7,1]

print("Largest:", largest(numbers))