#Decorators - wrap a function to add extra behavior
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished.")
        return result
    return wrapper

def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}!")

@timer
def countUp(n):
    total = sum(range(n))
    return total

greet("Sachin")
result = countUp(1000000)
print(f"Sum: {result}")
