#Count how many digits an integer has using a while loop
n = abs(int(input("Enter a number: ")))
count = 1

while n >= 10:
    n //= 10
    count += 1

print("Digits:", count)
