#Positional
def add(l,w):
    area = l*w
    return area

result = add(2,3)
print(f"Area: {result}")

#Default
def greet(name, msg = "Hi"):
    print(f"{msg},{name}")

greet("Sachin")
greet("SAAAAAA","Hello")

#Keyword
def info(name, age, city):
    print(f"{name}, {age}, {city}")

info(age=25, city = "KTM", name = "Sachin")


#Args/ kwargs
def total(*num):
    return sum(num)

def show(**info):
    for k,v in info.items():
        print(f"{k}:{v}")
