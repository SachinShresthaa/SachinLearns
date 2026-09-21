name = input("Enter name: ")
weight = float(input("Enter weight: "))
height = float(input("Enter Height: "))
BMI = weight / (height * height)

if BMI < 18.5:
    category = "Underweight"
elif BMI >= 18.5 and BMI <= 24.9:
    category = "Normal"
elif BMI >= 25 and BMI <= 29.9:
    category = "OverWeight"
else:
    category = "Obese"

print(f"Hi {name}! BMI :{BMI} Category: {category}")