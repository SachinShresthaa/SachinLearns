#Decorator that accepts arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

def validateInput(min_val, max_val):
    def decorator(func):
        def wrapper(value):
            if not (min_val <= value <= max_val):
                raise ValueError(f"Value must be between {min_val} and {max_val}")
            return func(value)
        return wrapper
    return decorator

@repeat(3)
def sayHi(name):
    print(f"Hi {name}!")

@validateInput(0, 100)
def setScore(score):
    print(f"Score set to: {score}")

sayHi("Sachin")

setScore(85)
try:
    setScore(150)
except ValueError as e:
    print(f"Error: {e}")
