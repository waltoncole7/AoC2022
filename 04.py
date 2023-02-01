# 3

with open("04d.txt") as file:
    input = file.read()
lines = input.split("\n")

output = 0
for line in lines:
    range1, range2 = line.split(',')
    lo1, up1 = [int(i) for i in range1.split("-")]
    lo2, up2 = [int(i) for i in range2.split("-")]
    # print(line, lo1, up1, lo2, up2, type(up1))
    if up1 <= up2 and lo1 >= lo2 or up1 >= up2 and lo1 <= lo2 or up1 >= lo2 and up1 <= up2 or lo1 >= lo2 and lo1 <= up2:
        output += 1

print(output)