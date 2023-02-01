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

def scoreOf(h, d):
    height = int(lines[h][d])
    score = 1
    thisDir = 0
    for tree in lines[h][:d][::-1]:
        comp = int(tree)
        if comp < height:
            thisDir += 1
        if comp >= height:
            thisDir += 1
            break
    score *= thisDir
    thisDir = 0
    for tree in lines[h][d+1:]:
        comp = int(tree)
        if comp < height:
            thisDir += 1
        if comp >= height:
            thisDir += 1
            break
    score *= thisDir
    thisDir = 0
    for tree in cols[d][:h][::-1]:
        comp = int(tree)
        if comp < height:
            thisDir += 1
        if comp >= height:
            thisDir += 1
            break
    score *= thisDir
    thisDir = 0
    for tree in cols[d][h+1:]:
        comp = int(tree)
        if comp < height:
            thisDir += 1
        if comp >= height:
            thisDir += 1
            break
    score *= thisDir
    return score

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
    
scoreOf(2,0)

maxScore = 0
for h in range(len(lines)):
    for j in range(len(lines[0])):
        thisScore = scoreOf(h,j)
        if thisScore > maxScore:
            maxScore = thisScore
print(maxScore)