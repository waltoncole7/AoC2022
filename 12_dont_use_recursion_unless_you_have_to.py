import copy, math
from termcolor import colored

#

with open("12d.txt") as file:
    input = file.read()
lines = input.split('\n')
for i in range(len(lines)):
    if 'S' in lines[i]:
        Sx = lines[i].index('S')
        Sy = i
    if 'E' in lines[i]:
        Ex = lines[i].index('E')
        Ey = i

myX = Sx
myY = Sy
maxX = len(lines[0])
maxY = len(lines)
# print(Ex, Ey)
def overlayMoves(moves, lines):
    for move in moves:
        lines[move[1]] = lines[move[1]][:move[0]] + 'X' + lines[move[1]][move[0] + 1:]
    for line in lines:
        print(line)

def heightDifference(x1, y1, x2, y2):
    height1 = lines[y1][x1]
    # print(x2, y2, maxX, maxY)
    height2 = lines[y2][x2]
    if x1 == Sx and y1 == Sy:
        height1 = 'a'
    if x2 == Ex and y2 == Ey:
        height2 = 'z'
    return ord(height2) - ord(height1)

def fitness(move, x, y):
    heightFitness = heightDifference(x, y, x+move[0], y+move[1]) #between -25 and 1
    if heightFitness == 1:
        heightFitness = 10000
    elif heightFitness == 0:
        heightFitness = 1000
    else:
        heightFitness += 25
    angleFitness = math.pi - math.acos(float(move[0]*(Ex-x)+move[1]*(Ey-y))/(math.sqrt((Ex-x)**2+(Ey-y)**2))) # between 0 and pi
    totalFitness = heightFitness + angleFitness * 200
    # print(move, x, y, heightFitness, angleFitness, totalFitness)
    return totalFitness

doNotReturn = []
moveCount = 0
def nextMove(previousSquares, x, y):
    moveValue = 0
    # print(lines[y][x], x, y)
    # if x == 132 or x == 131 or x == 133:
        # print(x, y)
    if x == Ex and y == Ey:
        print(len(previousSquares))
        print(overlayMoves(previousSquares, lines))
        return 1
    if len(previousSquares) > 550:
        return 1

    possibleMoves = [[1, 0], [0, -1], [0, 1], [-1, 0]] #Right, up, down, left
    if x == 0 or [x-1, y] in previousSquares or [x-1, y] in doNotReturn or heightDifference(x, y, x-1, y) > 1:
        possibleMoves.pop(3)
    if y == maxY - 1 or [x, y+1] in previousSquares or [x, y+1] in doNotReturn or heightDifference(x, y, x, y+1) > 1:
        possibleMoves.pop(2)
    if y == 0 or [x, y-1] in previousSquares or [x, y-1] in doNotReturn or heightDifference(x, y, x, y-1) > 1:
        possibleMoves.pop(1)
    if x == maxX - 1 or [x+1, y] in previousSquares or [x+1, y] in doNotReturn or heightDifference(x, y, x+1, y) > 1:
        possibleMoves.pop(0)

    #Could sort moves by directional fitness here later if needed
    # for move in possibleMoves:
    #     print(x, y, Sx, Sy)
    #     fitness = -math.acos(move[0]*(Sx-x)+move[1]*(Sy-y)/(math.sqrt((Ex-x)**2+(Ey-y)**2)))
    #     fitnesses.append(fitness)
    # print(x, y, Ex, Ey, possibleMoves)
    sortedMoves = sorted(possibleMoves, key=lambda move: -fitness(move, x, y))
    # print(x, y, sortedMoves)
    newPreviousSquares = copy.deepcopy(previousSquares)
    newPreviousSquares.append([x,y])
    for move in sortedMoves:
        moveValue += nextMove(newPreviousSquares, x+move[0], y+move[1])
    

    if moveValue == 0:
        doNotReturn.append([x,y])
    return moveValue

print(nextMove([], Sx, Sy))
print(overlayMoves(doNotReturn, lines))