
with open("05d.txt") as file:
    input = file.read()
lines = input.split("\n")
# print(lines)
start = lines[:8]
# print(start)
cols = [[] for i in range(9)] # Boxes sorted top to bototm
for i in range(9):
    # print(i)
    location = 1 + 4*i
    cols[i] = [row[location] for row in start if row[location] != ' ']
# print(cols)

moves = [[int(line.split(' ')[1]), int(line.split(' ')[3])-1, int(line.split(' ')[5])-1] for line in lines[10:]] #number, source, dest
# print(moves)

for move in moves:
    print(move)
    number = move[0]
    source = move[1]
    dest = move[2]
    print(cols)
    cols[dest] = cols[source][0:number] + cols[dest]
    print(cols)
    cols[move[1]] = cols[move[1]][number:]
    print(cols)

    # for i in range(move[0]):

        # box = cols[move[1]][0]
        # cols[move[1]] = cols[move[1]][1:]
        # cols[move[2]] = [box] + cols[move[2]]

# print(cols)
output = ""
for col in cols:
    if len(col) > 0:
        output += col[0]
print(output)