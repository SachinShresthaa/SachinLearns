name = input("Enter Name: ")
age = int(input("Enter Age: "))
citizen = input("Are you Nepali citizen? (yes/no): ")

if age >= 18 and citizen.lower() == "yes":
    print(name, "is eligible to vote")
else:
    print(name, "is not eligible to vote")