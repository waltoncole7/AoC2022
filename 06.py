# 7 Minutes

with open("06d.txt") as file:
    input = file.read()
lines = input.split("\n")

buffer = lines[0]

found = False
for i in range(14,len(buffer)):
    isStart = True
    if found:
        break
    possible = buffer[i-14:i]
    for char in possible:
        if possible.count(char) != 1:
            isStart = False
            break
    if isStart:
        print(i)
        found = True
        break
    
        