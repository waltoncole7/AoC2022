#

with open("09d.txt") as file:
    input = file.read()
moves = input.split("\n")

'''moves = []
i=0
for line in lines:
    moves.append([])
    moves[i] = 0
    moves[i][0] = line[0]
    moves[i][1] = int(line.split(' ')[1]) # move is [direction, int(distance)]
    i+= 1'''

xVals = [1000 for i in range(10)]
yVals = [1000 for i in range(10)]
print(xVals, yVals)

visited = set()

for move in moves:
    direction = move[0]
    for i in range(int(move[2:])):
        if direction == 'R':
            xVals[0] += 1
        elif direction == 'L':
            xVals[0] -= 1
        elif direction == 'D':
            yVals[0] += 1
        elif direction == 'U':
            yVals[0] -= 1


        for i in range(1, 10):
            # print(i)
            xDif = xVals[i-1] - xVals[i]
            yDif = yVals[i-1] - yVals[i]
            if xDif == 0 or yDif == 0:
                if xDif > 1:
                    xVals[i] += 1
                elif xDif < -1:
                    xVals[i] -= 1
                elif yDif > 1:
                    yVals[i] += 1
                elif yDif < -1:
                    yVals[i] -= 1
            elif abs(xDif) > 1 or abs(yDif) > 1:
                if xDif > 0:
                    xVals[i] += 1
                elif xDif < 0:
                    xVals[i] -= 1
                if yDif > 0:
                    yVals[i] += 1
                elif yDif < 0:
                    yVals[i] -= 1
        


        visited.add(xVals[9]*1003 + yVals[9]*1005)
        print(xVals, yVals)

print(len(visited))
