with open("14d.txt") as file:
    input = file.read()
lines = input.split('\n')

xMin = 480
xMax = 1000
yMin = 0
yMax = 174

grid = [['.' for j in range(xMax)] for i in range(yMax - yMin-1)]
grid.append(['#' for i in range(xMax)])

def printGrid(grid):
    firstRow = ' ' * (20)
    firstRow = firstRow[:20] + '500'
    print(firstRow)
    secondRow = [i % 10 for i in range(xMax)][xMin:xMin+200]
    rowString = ''
    for ind in secondRow:
        rowString += str(ind)
    print(rowString)
    for row in grid:
        rowString = ''
        for item in row[xMin:xMin+200]:
            rowString += item
        print(rowString)
        
# printGrid(grid)

def drawSegment(point1, point2, grid):
    point1 = [int(i) for i in point1.split(',')]
    point2 = [int(i) for i in point2.split(',')]
    if point1[0] == point2[0]: #Segment is vertical
        if point1[1] > point2[1]: #Right to left
            for rowIndex in range(point2[1], point1[1] + 1):
                grid[rowIndex][point1[0]] = '#'
        else:
            for rowIndex in range(point1[1], point2[1] + 1):
                # print(rowIndex, point1[0], len(grid), len(grid[0]))
                grid[rowIndex][point1[0]] = '#'
    else: # horizontal
        if point1[0] > point2[0]: #Bottom to top
            for colIndex in range(point2[0], point1[0] + 1):
                grid[point1[1]][colIndex] = '#'
        else:
            for colIndex in range(point1[0], point2[0] + 1):
                grid[point1[1]][colIndex] = '#'


for line in lines:
    points = line.split(' -> ')
    firstPoint = points[0]
    for point in points[1:]:
        drawSegment(firstPoint, point, grid)
        firstPoint = point
printGrid(grid)

def drop(grid):
    sandX = 500
    sandY = 0
    while grid[0][500] == '.':
        nextRow = grid[sandY+1]
        if nextRow[sandX] == '.':
            sandY += 1
        elif nextRow[sandX - 1] == '.':
            sandY += 1
            sandX -= 1
        elif nextRow[sandX + 1] == '.':
            sandY += 1
            sandX += 1
        else:
            grid[sandY][sandX] = 'o'
            # printGrid(grid)
            return False
    # printGrid(grid)
    return True

count = 0
while True:
    if drop(grid):
        print(count)
        break
    count += 1