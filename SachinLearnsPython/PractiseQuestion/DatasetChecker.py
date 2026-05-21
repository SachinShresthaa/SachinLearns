tr = int (input("Enter the total rows: "))
mr = int (input("Enter the Missing rows: "))
dr = int (input ("Enter the Duplicate rows: "))

cleanData = tr-(mr+dr)
cleanDataPercentage = float(cleanData/tr)*100

print(f"\nClean Data Percentage: {cleanDataPercentage:.2f}%")

if cleanDataPercentage >= 95:
    res = "Production ready"
elif cleanDataPercentage<95 and cleanDataPercentage>=80:
    res = "Needs Cleaning"
else:
    res = "Poor Data set"

print(f"\nDataset Status:: {res}")