model1 = float(input("Enter the accuracy of model 1 : "))
model2 = float(input("Enter the accuracy of model 2 : "))
model3 = float(input("Enter the accuracy of model 3 : "))

print(f"Model 1 : {model1:.2f}\nModel 2 : {model2:2f}\nModel 3 : {model3:.2f}")

if model1 > model2 and model1 > model3:
    res="Model 1 "
elif model2 > model1 and model2 > model3:
    res="Model 2 "
else:
    res="Model 3 "

print(f"Best Model is : {res}")

if model1>=90 and model2>=90 and model3>=90:
    print("All model is above 90%.")
else:
    print("All model is not above 90%.")

if model1<=70 or model2<=70 or model3<=70:
    print("Any of them are below 70")
else:
    print("None of them are below 70")

