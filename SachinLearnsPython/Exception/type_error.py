# type_error.py

try:
    result = "10" + 20
    print(result)

except TypeError:
    print("Cannot add string and integer.")