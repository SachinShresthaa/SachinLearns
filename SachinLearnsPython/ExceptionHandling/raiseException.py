#Raising exceptions manually with raise
def setAge(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age seems unrealistic")
    return age

#try/except/else - else runs only when no exception
def getAge(value):
    try:
        age = setAge(value)
    except (TypeError, ValueError) as e:
        print(f"Validation failed: {e}")
    else:
        print(f"Age set successfully: {age}")

getAge(25)
getAge(-5)
getAge("old")
getAge(200)
