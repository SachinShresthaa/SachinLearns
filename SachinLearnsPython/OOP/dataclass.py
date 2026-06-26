#dataclass - auto-generates __init__ __repr__ __eq__
from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    age: int
    score: float
    subjects: list = field(default_factory=list)

    def grade(self):
        if self.score >= 90: return "A"
        elif self.score >= 75: return "B"
        elif self.score >= 60: return "C"
        else: return "F"

s1 = Student("Sachin", 22, 88.5, ["Python", "ML"])
s2 = Student("Hero",   21, 95.0, ["AI", "Math"])
s3 = Student("Alice",  23, 88.5)

print(s1)                    #auto __repr__
print(s1 == s3)              #auto __eq__ compares fields
print(s1.grade())
print(s2.grade())

students = [s1, s2, s3]
top = max(students, key=lambda s: s.score)
print(f"Top student: {top.name}")
