# 
import copy

with open("07d.txt") as file:
    input = file.read()
lines = input.split("\n")


def getWorkingDirContents(indices):
    global filesystem
    digger = copy.deepcopy(filesystem)
    for index in indices:
        digger = digger[index][1]
    return digger

def setWorkingDirContents(system, indices, setter, new, external):
    if external:
        setter.append(new)
    if len(indices) > 0:
        setWorkingDirContents(system[indices[0]][1], indices[1:], setter, 0, False)
    else:
        print(id(system), id(filesystem[0][1]))
        system = setter
        print(id(system), id(filesystem[0][1]))


def discoverDir(type, name, parentIndices):
    if type == "dir":
        setWorkingDirContents(copy.copy(filesystem), parentIndices, getWorkingDirContents(parentIndices), [name, []], True)
        print(filesystem)
    else:
        setWorkingDirContents(copy.copy(filesystem) ,parentIndices, getWorkingDirContents(parentIndices).append([name, type]))
        print(filesystem)



filesystem = [['/', []]] # Each file/dir is in format [name, size/[contents]]

workingDirIndex = [0]
for line in lines:
    if line[0] == "$":
        if line[2] == "l":
            pass
        elif line[2] == "c":
            newDirName = line.split(' ')[2]
            if newDirName == '..':
                workingDirIndex.pop(-1)
            elif newDirName == '/':
                workingDirIndex = [0]
            else:
                workingDirContents = getWorkingDirContents(workingDirIndex)
                for i in range(len(workingDirContents)):
                    subDir = workingDirContents[i]
                    if subDir[0] == newDirName:
                        workingDirIndex.append(i)
            print(newDirName, workingDirIndex)
    else:
        discoverDir(line.split(' ')[0], line.split(' ')[1], workingDirIndex)
