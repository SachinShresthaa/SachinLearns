# creating lists
fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30, 40, 50]
mixed = [1, "hello", 3.14, True]

# accessing elements
print(fruits[0])        # apple
print(fruits[-1])       # mango (last item)
print(numbers[1:4])     # [20, 30, 40]

# modifying elements
fruits[1] = "grapes"
print(fruits)           # ['apple', 'grapes', 'mango']

# append - add to end
fruits.append("orange")
print(fruits)

# insert - add at specific position
fruits.insert(1, "kiwi")
print(fruits)

# remove - remove by value
fruits.remove("grapes")
print(fruits)

# pop - remove by index (returns the removed item)
removed = fruits.pop(0)
print("Removed:", removed)
print(fruits)

# extend - add multiple items
fruits.extend(["pineapple", "strawberry"])
print(fruits)

# length, min, max, sum
print(len(numbers))     # 5
print(min(numbers))     # 10
print(max(numbers))     # 50
print(sum(numbers))     # 150

# check if item exists
print("mango" in fruits)    # True
print("grape" in fruits)    # False
