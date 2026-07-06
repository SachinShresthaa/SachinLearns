f = open("data.txt","w")
f.write("Machine Learning")
f.write("Deep Learning")
f.close()

with open("data.txt","r" ,encoding="utf-8") as f:
    for line in f:
     print(line.strip())