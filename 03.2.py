# 19 Minutes :(

with open("03d.txt") as file:
    input = file.read()
lines = input.split("\n")

output = 0

for i in range(int(len(lines)/3)):
    a, b, c = lines[3*i:3*i+3]
    # print(a)
    for d in a:
        if d in b:
            if d in c:
                common = d
                break
    asc = ord(common)
    if asc > 94:
        toAdd = asc - 96
    else:
        toAdd = asc - 38
    output += toAdd
    # print(toAdd)
    



print(output)