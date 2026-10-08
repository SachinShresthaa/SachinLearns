#Show the balance at the end of each year with yearly compound interest
principal = float(input("Principal: "))
rate = float(input("Annual rate (%): "))
years = int(input("Years: "))
balance = principal

for year in range(1, years + 1):
    balance += balance * rate / 100
    print(f"Year {year}: {balance:.2f}")
