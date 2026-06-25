#Custom Exception Classes
class AgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}. Age must be between 0 and 150.")

class ScoreError(Exception):
    def __init__(self, score):
        self.score = score
        super().__init__(f"Invalid score: {score}. Score must be between 0 and 100.")

def registerStudent(name, age, score):
    if age < 0 or age > 150:
        raise AgeError(age)
    if score < 0 or score > 100:
        raise ScoreError(score)
    print(f"Student {name} registered! Age: {age}, Score: {score}")

try:
    registerStudent("Sachin", 22, 85)
    registerStudent("Hero", 200, 90)
except AgeError as e:
    print(f"AgeError caught: {e}")
except ScoreError as e:
    print(f"ScoreError caught: {e}")
