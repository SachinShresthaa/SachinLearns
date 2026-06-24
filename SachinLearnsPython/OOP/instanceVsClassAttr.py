#Instance vs Class Attributes
class Student:
    school = "Tribhuvan University"  #class attribute (shared)

    def __init__(self, name, grade):
        self.name = name    #instance attribute (unique)
        self.grade = grade

s1 = Student("Sachin", "A")
s2 = Student("Hero", "B")

print(s1.school)   #shared
print(s2.school)   #shared

print(s1.name)     #unique
print(s2.name)     #unique

#changing class attribute
Student.school = "Pokhara University"
print(s1.school)
print(s2.school)
