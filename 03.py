# 

with open("03d.txt") as file:
    input = file.read()
lines = input.split("\n")

output = 0
print(ord("a"))
for line in lines:
    a, b = line[0:int(len(line)/2)], line[int(len(line)/2):]
    for c in a:
        if c in b:
            common = c
            break
    asc = ord(common)
    if asc > 94:
        toAdd = asc - 96
    else:
        toAdd = asc - 38
    output += toAdd
    # print(toAdd)
    



print(output)