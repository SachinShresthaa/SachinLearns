confidence = float(input("Enter confidence score (0 to 1): "))
label = input("Enter prediction label: ").strip()

if label == "":
    print("Invalid Prediction")
else:
    if confidence >= 0.9:
        reliability = "Highly Reliable"
    elif 0.7 <= confidence < 0.9:
        reliability = "Moderately Reliable"
    else:
        reliability = "Unreliable Prediction"

    print(f"\nPrediction Label: {label}\nConfidence Score: {confidence}\nResult: {reliability}")