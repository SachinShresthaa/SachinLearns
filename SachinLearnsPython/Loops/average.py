#Find the average of a list of numbers without using sum() or len()
nums = [12, 45, 7, 89, 56, 34]
total = 0
count = 0

for n in nums:
    total += n
    count += 1

if count == 0:
    print("List is empty")
else:
    print("Average:", total / count)
