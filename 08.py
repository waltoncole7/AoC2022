#

with open("08d.txt") as file:
    input = file.read()
lines = input.split("\n")

cols = []
for i in range(len(lines[0])):
    row = ""
    for j in range(len(lines)):
        row += lines[j][i]
    cols.append(row)

def isVisible(h, d):
    height = int(lines[h][d])
    thisDir = True
    for tree in lines[h][:d]: #From left
        if int(tree) >= height:
            thisDir = False
            break
    if thisDir:
        return True
    thisDir = True
    for tree in lines[h][d+1:]: #From right
        if int(tree) >= height:
            thisDir = False
            break
    if thisDir:
        return True
    thisDir = True
    for tree in cols[d][:h]: #From top
        if int(tree) >= height:
            thisDir = False
            break
    if thisDir:
        return True
    thisDir = True
    for tree in cols[d][h+1:]: #From bottom
        if int(tree) >= height:
            thisDir = False
            break
    if thisDir:
        return True
    return False
    
count = 0
for h in range(len(lines)):
    for j in range(len(lines[0])):
        if isVisible(h,j):
            print(h,j,lines[h][j])
            count += 1
print(count)