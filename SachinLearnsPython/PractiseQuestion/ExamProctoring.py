fd = input("Face Detected (True/False): ")
md = input  ("Multiple Person detectd (True/False): ")
nl = int(input("Enter Noise Level: "))

condition = fd.lower() == "true" and md.lower()=="false" and nl <50 
if condition:
    print("Exam Environment Valid")
else:
    print("Exam Environment Invalid")

if fd.lower() == "false":
    print("Face not detected")

if md.lower()=="true":
    print("Multiple face detected")

if nl>=50:
    print("Too much noise")