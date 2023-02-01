from myobjects import sparseGrid3D
from queue import Queue

with open("18d.txt") as file:
    input = file.read()
lines = input.split('\n')


grid = sparseGrid3D()
for line in lines:
    x, y, z = [int(i) for i in line.split(',')]
    grid.set(x, y, z, 'O')


count = 0
frontier = Queue()
reached = set()
xMin, xMax, yMin, yMax, zMin, zMax = grid.extremes()

#Buffer to traverse around obsidian
xMin -= 1
yMin -= 1
zMin -= 1
xMax += 1
yMax += 1
zMax += 1

point = (xMin-1, yMin, zMin)
frontier.put(point)
while not frontier.empty():
    cell = frontier.get()
    x, y, z = cell
    # print(cell)
    for neighbor in grid.getNeighbors(cell):
        x, y, z = neighbor
        isObsidian = neighbor in grid
        isReached = neighbor in reached
        isInBounds = xMin <= x <= xMax and yMin <= y <= yMax and zMin <= z <= zMax
        if isInBounds and (not (isReached)) and (not (isObsidian)):
            frontier.put(neighbor)
            reached.add(neighbor)
        if isObsidian:
            count += 1
            # print(cell, neighbor)
print(count)
# print(reached)
