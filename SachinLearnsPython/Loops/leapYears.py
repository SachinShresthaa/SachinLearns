#Print all leap years between two given years (inclusive)
start = int(input("Start year: "))
end = int(input("End year: "))

for year in range(start, end + 1):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, end=" ")
