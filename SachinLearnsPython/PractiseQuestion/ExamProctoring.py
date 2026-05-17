faceDetction = input("Face Detected (True/False): ")
multipleDetected = input  ("Multiple Person detectd (True/False): ")
noiseLevel = int(input("Enter Noise Level: "))

condition = faceDetction.lower() == "true" and multipleDetected.lower()=="false" and noiseLevel <50 
if condition:
    print("Exam Environment Valid")
else:
    print("Exam Environment Invalid")

if faceDetction.lower() == "false":
    print("Face not detected")

if multipleDetected.lower()=="true":
    print("Multiple face detected")

if noiseLevel>=50:
    print("Too much noise")