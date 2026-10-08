#Print all perfect squares up to a user given limit without using sqrt() or **
limit = int(input("Limit: "))
i = 1

while i * i <= limit:
    print(i * i, end=" ")
    i += 1
