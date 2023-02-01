from myobjects import sparseGrid
from copy import deepcopy
with open("17d.txt") as file:
    jetPattern = file.read()
    
patternLength = len(jetPattern)

beam = ['#', '#', '#', '#']
plus = [['.', '#', '.'], ['#', '#', '#'], ['.', '#', '.']]
l = [['.', '.', '#'], ['.', '.', '#'], ['#', '#', '#']]
i = [['#'], ['#'], ['#'], ['#']]
square = [['#', '#'], ['#', '#']]
rockPatterns = (beam, plus, l, i, square)
rocks = []
for rockPattern in rockPatterns:
    rocks.append(sparseGrid(rockPattern))
print(rocks)
for rock in rocks:
    rock.printGrid()
    print('\n')

def outOfBounds(squid):
    for item in squid:
        if item[0] > 7 or item[0] < 0:
            return False
    return True


xBounds = (0,7)
board = sparseGrid(['#' for i in range(8)])
rocksBackup = deepcopy(rocks)
height = 0
j = 0
for i in range(2022):
    rock = rocks[i % 5]
    rock.shift((2, -height - 3))

    # Drop piece
    while True:
        jetDirection = jetPattern[j % patternLength]
        j+= 1
        print(i)
        movingDown = False

        if movingDown:
            down = rock.shift((0, 1))
            if board.overlaps(down):
                board.merge(rock)
                break
            else:
                rock = down
        else:
            if jetDirection == '>':
                right = rock.shift((1, 0))
                if not(outOfBounds(right) or board.overlaps(right)):
                    rock = right
            else:
                left = rock.shift((-1, 0))
                if not(outOfBounds(left) or board.overlaps(left)):
                    rock = left




        movingDown = not movingDown        
    rocks = deepcopy(rocksBackup)
    height = board.extremes()[2]
print(height)