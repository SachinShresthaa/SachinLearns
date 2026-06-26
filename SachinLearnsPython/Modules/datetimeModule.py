#datetime module - working with dates and times
from datetime import datetime, date, timedelta

#current date and time
now = datetime.now()
today = date.today()
print(now)
print(today)

#formatting
print(now.strftime("%d/%m/%Y %H:%M:%S"))
print(now.strftime("%B %d, %Y"))          #June 26, 2026

#parsing string to datetime
dob = datetime.strptime("2003-05-15", "%Y-%m-%d")
print(f"Born: {dob.strftime('%B %d, %Y')}")

#timedelta - date arithmetic
age = today - dob.date()
print(f"Days alive: {age.days}")

deadline = today + timedelta(days=30)
print(f"Deadline: {deadline}")

#comparing dates
d1 = date(2026, 1, 1)
d2 = date(2026, 12, 31)
print(f"Days left in year: {(d2 - today).days}")
