#Given a list of integers, count how many are even and how many are odd using a single for loop
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count = 0
odd_count = 0
for n in nums:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even count: ", even_count)
print("Odd count: ", odd_count)