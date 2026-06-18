#Tuple creation 
point = (910.5, 20.3)
rgb = (255,128,0)
person = ("sachin",22,"BCA")

#Turple as dict key (list cant do this!)
locations = {(28.5, 77.2): "Manthali",
             (19.0,72.8): "Heriiiiiiii"}

print(locations[(28.5,77.2)])

#singe-element tuple = need trainling comma
one = (42,)
print(type(one))
