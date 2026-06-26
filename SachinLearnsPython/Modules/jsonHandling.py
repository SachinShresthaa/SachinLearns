#JSON handling - json module
import json
import os

student = {
    "name": "Sachin",
    "age": 22,
    "scores": [88, 95, 72],
    "active": True,
    "address": {"city": "Kathmandu", "country": "Nepal"}
}

#dict to JSON string
json_str = json.dumps(student, indent=2)
print(json_str)

#JSON string back to dict
parsed = json.loads(json_str)
print(parsed["address"]["city"])

#write JSON to file
with open("student.json", "w") as f:
    json.dump(student, f, indent=2)

#read JSON from file
with open("student.json", "r") as f:
    loaded = json.load(f)
    print(f"Loaded: {loaded['name']}, scores: {loaded['scores']}")

os.remove("student.json")   #cleanup
