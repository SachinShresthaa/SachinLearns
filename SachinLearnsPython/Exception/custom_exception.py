# custom_exception.py

class InvalidAgeError(Exception):
    pass

age = int(input("Enter age: "))

try:
    if age < 18:
        raise InvalidAgeError("You are not eligible.")

    print("Welcome!")

except InvalidAgeError as e:
    print(e)