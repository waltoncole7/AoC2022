# 19, 50 mins

with open("10d.txt") as file:
    input = file.read()
lines = input.split("\n")

screen = ['.' * 40 for j in range(6)]

def printScreen(CRT):
    for row in CRT:
        print(row)
        

checkCycles = [20 + 40*i for i in range(6)]
x = 1
cycle = 1
output = 0
for line in lines:
    if cycle in checkCycles:
        output += cycle * x
        # print('b', cycle, x)
    if line == 'noop':




        # Do stuff (this is happening during current cycle)
        row = (cycle-1) // 40
        col = (cycle-1) % 40
        if x == col or x+1 == col or x-1 == col:
            screen[row] = screen[row][:col] + "#" + screen[row][col + 1:]
            print(cycle, x, row, col)


        cycle += 1
    

    else:





        #Do stuff twice (this is happening during current cycle)
        row = (cycle-1) // 40
        col = (cycle-1) % 40
        if x == col or x+1 == col or x-1 == col:
            print(cycle, x, row, col)
            screen[row] = screen[row][:col] + "#" + screen[row][col + 1:]
        secondCycle = cycle
        row = secondCycle // 40
        col = secondCycle % 40
        # if previousLine[0] == 'a':
        #     secondX = x + int(previousLine[5:])
        # else:
            # secondX = x
        secondX = x
        if secondX == col or secondX+1 == col or secondX-1 == col:
            screen[row] = screen[row][:col] + "#" + screen[row][col + 1:]
            print(secondCycle, x, row, col)




        # print(line, x, cycle)
        if cycle + 1 in checkCycles:
            output += (cycle+1) * x
            # print('a', cycle+1, x)
        x += int(line[5:])
        cycle += 2
    previousLine = line



print(output)
printScreen(screen)
