# Tuple creation
point = (10.5, 20.3)
rgb = (255, 128, 0)
person = ("sachin", 22, "BCA")

# Tuple as dict key (list can't do this!)
locations = {(28.5, 77.2): "Manthali",
             (19.0, 72.8): "Mumbai"}

print(locations[(28.5, 77.2)])

# Single-element tuple needs trailing comma
one = (42,)
