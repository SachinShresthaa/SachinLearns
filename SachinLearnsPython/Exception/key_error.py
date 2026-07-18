# key_error.py

student = {
    "name": "Sachin",
    "age": 20
}

try:
    print(student["address"])

except KeyError:
    print("Key not found.")