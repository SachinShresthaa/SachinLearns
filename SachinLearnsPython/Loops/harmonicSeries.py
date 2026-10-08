#Compute the harmonic series 1 + 1/2 + 1/3 + ... + 1/N using a for loop
n = int(input("N: "))
total = 0

for i in range(1, n + 1):
    total += 1 / i

print(f"Sum: {total:.4f}")
