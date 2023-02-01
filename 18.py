from myobjects import sparseGrid3D

with open("18d.txt") as file:
    input = file.read()
lines = input.split('\n')


grid = sparseGrid3D()
for line in lines:
    x, y, z = [int(i) for i in line.split(',')]
    grid.set(x, y, z, 'O')

count = 0
for block in grid:
    # print(block)
    neighbors = grid.getNeighbors(block)
    for neighbor in neighbors:
        if neighbor not in grid:
            count += 1
print(count)
