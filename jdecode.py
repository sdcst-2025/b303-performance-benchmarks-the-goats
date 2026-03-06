import json

f = open("jsontest","r")
imported = f.readline()
print(imported)
x = json.loads(imported)
print(f" x variable is of type : {type(x)} {x}")