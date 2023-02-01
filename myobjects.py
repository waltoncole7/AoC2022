

class sparseGrid(dict):
    def __init__(self):
        self.defaultValue = '.'
    def __init__(self, state=[[]]):
        self.defaultValue = '.'
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] != '.':
                    self.set((j, i), '#')
    
    def get(self, coords):
        if coords in self:
            return self[coords]
        return self.defaultValue
    def set(self, coords, value):
        self[coords] = value
    def getNeighbors(self, coords):
        x, y = coords
        output = []
        for neighborDirection in self.neighborDirections:
            neighbor = (neighborDirection[0] + x, neighborDirection[1] + y)
            output.append(neighbor)
        return output
    def getNeighbors(self, coords):
        x, y = coords
        output = []
        for neighborDirection in self.neighborDirections:
            neighbor = (neighborDirection[0] + x, neighborDirection[1] + y)
            output.append(neighbor)
        return output
    def extremes(self): #returns list of xmin, xmax, ymin, ymax
        for item in self:
            x, y = item
            break
        output = [x, x, y, y]
        for point in self:
            if point[0] < output[0]:
                output[0] = point[0]
            if point[0] > output[1]:
                output[1] = point[0]
            if point[1] < output[2]:
                output[2] = point[1]
            if point[1] > output[3]:
                output[3] = point[1]
        return output
    def shift(self, coords):
        newGrid = sparseGrid()
        x, y = coords
        for object in self:
            newGrid.set((object[0] + x, object[1] + y), self[object])
        self = newGrid
        return self
    def printGrid(self):
        extremes = self.extremes()
        for y in range(extremes[2], extremes[3]+1):
            row = ''
            for x in range(extremes[0], extremes[1]+1):
                row += self.get((x, y))
            print(row)
    def merge(self, otherGrid):
        for each in otherGrid:
            self.set(each, otherGrid[each])
    def overlaps(self, otherGrid):
        for each in otherGrid:
            if each in self:
                return True
        return False

class sparseGrid3D(dict):
    def __init__(self):
        self.defaultValue = '.'
        self.neighborDirections = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    def get(self, x, y, z):
        if (x, y, z) in self:
            return self[(x, y, z)]
        return self.defaultValue
    def set(self, x, y, z, value):
        self[(x, y, z)] = value
    def getNeighbors(self, x, y, z):
        output = []
        for neighborDirection in self.neighborDirections:
            neighbor = (neighborDirection[0] + x, neighborDirection[1] + y, neighborDirection[2] + z)
            output.append(neighbor)
        return output
    def getNeighbors(self, coords):
        x, y, z = coords
        output = []
        for neighborDirection in self.neighborDirections:
            neighbor = (neighborDirection[0] + x, neighborDirection[1] + y, neighborDirection[2] + z)
            output.append(neighbor)
        return output
    def extremes(self): #returns list of xmin, xmax, ymin, ymax, zmin, zmax
        for item in self:
            x, y, z = item
            break
        output = [x, x, y, y, z, z]
        for point in self:
            if point[0] < output[0]:
                output[0] = point[0]
            if point[0] > output[1]:
                output[1] = point[0]
            if point[1] < output[2]:
                output[2] = point[1]
            if point[1] > output[3]:
                output[3] = point[1]
            if point[2] < output[4]:
                output[4] = point[2]
            if point[2] > output[5]:
                output[5] = point[2]
        return output
        

