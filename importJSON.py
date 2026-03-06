import json

x = [ 1, 2, 3, 4, 5]

encoded = json.dumps(x)

print(f" encoded variable is of type : {type(encoded)} {encoded}")
print(f" x variable is of type : {type(x)} {x}")

f = open("jsontest","w")
f.write(encoded)
f.close()