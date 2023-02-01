#
from queue import Queue

with open("12d.txt") as file:
    input = file.read()
lines = input.split('\n')
for i in range(len(lines)):
    if 'S' in lines[i]:
        sX = lines[i].index('S')
        sY = i
    if 'E' in lines[i]:
        eX = lines[i].index('E')
        eY = i

lines[sY] = lines[sY][:sX] + 'a' + lines[sY][1+sX:]
lines[eY] = lines[eY][:eX] + 'z' + lines[eY][1+eX:]

maxX = len(lines[0]) - 1
maxY = len(lines) - 1
possibleStarts = []

allNodeLocations = []
for x in range(len(lines[0])):
    for y in range(len(lines)):
        allNodeLocations.append((x, y))
        if lines[y][x] == 'a':
            possibleStarts.append((x, y))

def height(nodeLocation):
    return ord(lines[nodeLocation[1]][nodeLocation[0]])

def neighbors(nodeLocation):
    output = []
    neighborDirections = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    for direction in neighborDirections:
        newNodeLocation = (nodeLocation[0] + direction[0], nodeLocation[1] + direction[1])
        if 0 <= newNodeLocation[0] < len(lines[0]) and 0 <= newNodeLocation[1] < len(lines) and height(newNodeLocation) - height(nodeLocation) <= 1:
            output.append(newNodeLocation)
    return output

possibleLengths = []
# possibleStarts = [(sX, sY)]
for possibleStart in possibleStarts:
    # print(possibleStart)
    sX, sY = possibleStart
    cameFrom = dict()
    frontier = Queue()
    frontier.put((sX, sY))
    reached = set()
    reached.add((sX, sY))
    cameFrom[(sX, sY)] = None
    # print(frontier.empty())
    while not frontier.empty():
        thisSquare = frontier.get()
        # print(thisSquare)
        for square in neighbors(thisSquare):
            if square not in reached:
                cameFrom[square] = thisSquare
                frontier.put(square)
                reached.add(square)
    currentIndex = (eX, eY)
    # print(currentIndex)
    count = 0
    if (eX, eY) in reached:
        while True:
            if currentIndex == (sX, sY):
                possibleLengths.append(count)
                break
            count += 1
            currentIndex = cameFrom[currentIndex]
print(sorted(possibleLengths)[0])