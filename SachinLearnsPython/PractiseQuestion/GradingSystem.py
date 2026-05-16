python_marks = float(input("Enter Python marks: "))
statistics_marks = float(input("Enter Statistics marks: "))
ml_marks = float(input("Enter Machine Learning marks: "))

# Calculate average
average = (python_marks + statistics_marks + ml_marks) / 3

print("\nAverage Marks:", average)

# Grade assignment
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

# AI Career Recommendation
if average > 85:
    recommendation = "AI Engineer"
elif average > 70:
    recommendation = "Data Analyst"
else:
    recommendation = "Software Developer"

print("Career Recommendation:", recommendation)