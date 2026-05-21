python = float(input("Enter Python marks: "))
statistics = float(input("Enter Statistics marks: "))
ml = float(input("Enter Machine Learning marks: "))

average = (python + statistics + ml) / 3

print("\nAverage Marks:", average)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if average > 85:
    recommendation = "AI Engineer"
elif average > 70:
    recommendation = "Data Analyst"
else:
    recommendation = "Software Developer"

print("Career Recommendation:", recommendation)