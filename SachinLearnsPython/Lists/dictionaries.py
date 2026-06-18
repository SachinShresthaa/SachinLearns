#Creating a dictonary
Student = {
    "name":"SACHIN",
    "age":22,
    "scores":[85,92,78],
    "active":True
}
#access
print(Student["name"]) #direct access
print(Student.get("grade","N/A")) #safe access

#Add/update
Student["grade"]="A"
Student["age"]=23

#Neested dict
db = {"u1":{"name":"SAChin","score":90},
      "u2":{"name":"HEROOO","score":100}}

print(db["u1"]["score"])