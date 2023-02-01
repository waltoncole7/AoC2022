from queue import PriorityQueue

with open("testd.txt") as file:
    input = file.read()
lines = input.split('\n')

class room():
    def __init__(self, name, flowRate, neighbors):
        self.name = name
        self.flowRate = flowRate
        self.neighbors = neighbors
        self.turnedValve = False
    def __str__(self):
        return self.name

rooms = set()
roomsByName = dict()
for line in lines:
    name = line.split('Valve ')[1].split(' has')[0]
    flowRate = int(line.split('rate=')[1].split(';')[0])
    # print(line)
    if line.split('valve')[1][0] == 's':
        neighbors = line.split('valves ')[1].split(', ')
    else:
        neighbors = line.split('valve ')[1].split(', ')
    thisRoom = room(name, flowRate, neighbors)
    roomsByName[name] = thisRoom
    if name == 'AA':
        startingRoom = thisRoom
    rooms.add(thisRoom)

def maxScore(currentRoom, gasSoFar, time):
    if time == 0:
        return gasSoFar
    # print(currentRoom, gasSoFar, time)
    if time > 10:
        print(time)
    moves = currentRoom.neighbors
    scores = []
    if not currentRoom.turnedValve and currentRoom.flowRate != 0:
        scores.append(maxScore(currentRoom, gasSoFar + currentRoom.flowRate * time, time - 1))
        currentRoom.turedValve = True
    if len(moves) == 0:
        return gasSoFar
    for move in moves:
        scores.append(maxScore(roomsByName[move], gasSoFar, time - 1))
    highest = max(scores)
    return max(scores)



print(maxScore(roomsByName['AA'], 0, 30))