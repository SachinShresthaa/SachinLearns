CGPA = float(input("Enter CGPA : "))
Percentage = float(input("Enter Attendence Percentage : "))
Baclogs = int(input("Enter the number of Backlogs : "))

if CGPA >= 3.7 and Percentage >= 85 and Baclogs == 0:
    print("Full Scholarship")
elif CGPA >= 3.2 and Percentage >=75:
    print("Partial Scholarship")
else:
    print("Not Eligible")

print (f"\nCGPA : {CGPA}\nPercentage : {Percentage}\nBacklogs : {Baclogs}")