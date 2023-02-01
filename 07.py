# 2h:35m :(((

with open("07d.txt") as file:
    input = file.read()
lines = input.split("\n")

class object:
    global globalSum
    def __init__(self, name, type, value, parent):
        self.name = name
        self.type = type
        self.value = value
        self.parent = parent
    
    def addObject(self, newObject):
        self.value.append(newObject)

    def getSubDir(self, name):
        for item in self.value:
            if item.name == name:
                return item

    def getParentDir(self):
        return self.parent

    def getSize(self):
        part1 = 0
        size = 0
        if self.type == 'file':
            size = self.value
        else:
            for item in self.value:
                size += item.getSize()
        if size >= 4359867 and size <= 5359867 and self.type == 'dir':
            print(self, size)
            part1 += size
        return size
    
    def __str__(self):
        return self.name
    

filesystem = object("/", "dir", [], None)

workingDir = filesystem
for line in lines:
    if line[0] == "$" and line[2] == 'c':
        if line[5] == '/':
            workingDir = filesystem
        elif line[5:7] == '..':
            workingDir = workingDir.getParentDir()
        else:
            name = line[5:]
            workingDir = workingDir.getSubDir(name)

    elif line[0] != '$':
        data, name = line.split(' ')
        if data == 'dir':
            workingDir.addObject(object(name, 'dir', [], workingDir))
        else:
            workingDir.addObject(object(name, 'file', int(data), workingDir))
    # print(filesystem, workingDir, line)

print(filesystem.getSize()-40000000)









# testObject = object("bob", "dir", [object('a', 'file', 100, 'bob'), object('b', 'file', 200, 'bob')], "/")
# print(testObject.getSize())