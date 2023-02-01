with open("15d.txt") as file:
    input = file.read()
lines = input.split('\n')

class sparseGrid(dict):
    def __init__(self):
        self.defaultValue = '.'
    def get(self, x, y):
        if (x, y) in self:
            return self[(x, y)]
        return self.defaultValue
    def set(self, x, y, value):
        self[(x, y)] = value

def manhattan(tup1, tup2):
    return abs(tup1[0] - tup2[0]) + abs(tup1[1] - tup2[1])

grid = sparseGrid()
sensors = set()
beacons = set()
sensorDist = dict()
sensorClosestBeacons = dict()

for line in lines:
    sX = int(line.split('x=')[1].split(',')[0])
    sY = int(line.split('y=')[1].split(':')[0])
    bX = int(line.split('x=')[2].split(',')[0])
    bY = int(line.split('y=')[2])
    grid.set(sX, sY, 'S')
    sensors.add((sX, sY))
    grid.set(bX, bY, 'B')
    beacons.add((bX, bY))
    sensorClosestBeacons[(sX, sY)] = (bX, bY)
    sensorDist[(sX, sY)] = manhattan((sX, sY), (bX, bY))
    
# print(manhattan((1, 16), (-20, 12)))


    # for sensor in sensors:

    #     distances = dict()
    #     for beacon in beacons:
    #         distances[beacon] = manhattan(sensor, beacon)
    #     # print(distances[sorted(distances, key = lambda x: distances[x])[0]])
    #     # print(sorted(distances, key = lambda x: distances[x]), distances[(15, 3)])
    #     minDistance = sorted(distances, key = lambda x: distances[x])[0][0]
    #     sensorDist[sensor] = minDistance
    #     # print(sensor, minDistance)
            
            
xMin = -10000000
xMax = 10000000
y = 2000000
count = 0

for x in range(xMin, xMax):
    for sensor in sensors:
        checkToSensor = manhattan((x, y), sensor)
        beaconToSensor = sensorDist[sensor]
        # print(checkToSensor, beaconToSensor)
        if checkToSensor <= beaconToSensor and (x,y) not in beacons:
            count += 1
            break
    if x % 100000 == 0:
        print(x)
print(count)

