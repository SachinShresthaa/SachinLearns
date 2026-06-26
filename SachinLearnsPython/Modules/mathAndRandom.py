#math and random modules
import math
import random

#math module
print(math.sqrt(144))
print(math.pi)
print(math.ceil(4.2))
print(math.floor(4.9))
print(math.pow(2, 10))
print(math.log(1000, 10))   #log base 10

#random module
print(random.randint(1, 100))         #random int
print(random.random())                #float between 0-1
print(random.uniform(1.5, 9.5))      #random float in range

items = ["Python", "ML", "AI", "Data"]
print(random.choice(items))           #pick one
random.shuffle(items)
print(items)                          #shuffled list
print(random.sample(items, 2))        #pick 2 without repeat
