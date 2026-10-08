#Count how many times each digit 0-9 appears in an integer
n = abs(int(input("Enter a number: ")))
counts = [0] * 10

if n == 0:
    counts[0] = 1
while n > 0:
    counts[n % 10] += 1
    n //= 10

for digit in range(10):
    if counts[digit] > 0:
        print(f"{digit}: {counts[digit]}")
