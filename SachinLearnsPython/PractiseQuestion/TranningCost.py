th = float(input("Enter number of training hours: "))
ghc = float(input("Enter GPU hourly cost: "))
sc = float(input("Enter storage cost: "))

total_cost = (th * ghc) + sc

print("\nTotal Training Cost:", total_cost)

if total_cost > 100000:
    scale = "Enterprise Scale Training"
elif total_cost > 50000:
    scale = "Mid Scale Training"
else:
    scale = "Small Scale Experiment"

print("Training Category:", scale)