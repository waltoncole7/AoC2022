with open("testd.txt") as file:
    input = file.read()
lines = input.split('\n')

class monkey(): #TYPE EITHER "num" or "op"
    def __init__(self, name, type, value, operation, monkey1, monkey2):
        self.name = name
        self.type = type
        if self.type == 'num':
            self.value = int(value)
        else:
            self.operation = operation
            self.monkey1 = monkey1
            self.monkey2 = monkey2
    
    def yell(self):
        if self.type == 'num':
            return self.value
        else:
            if self.operation == '+':
                return getMonkey(self.monkey1).yell() + getMonkey(self.monkey2).yell()
            if self.operation == '-':
                return getMonkey(self.monkey1).yell() - getMonkey(self.monkey2).yell()
            if self.operation == '*':
                return getMonkey(self.monkey1).yell() * getMonkey(self.monkey2).yell()
            if self.operation == '/':
                return getMonkey(self.monkey1).yell() // getMonkey(self.monkey2).yell()
            print("BROKEN")
            return None
    
    def hasHuman(self):
        if self.name == 'humn':
            return True
        if self.type == 'num':
            return False
        return getMonkey(self.monkey1).hasHuman() or getMonkey(self.monkey2).hasHuman()

def getMonkey(name):
    return monkeys[name]

monkeys = dict()

for line in lines:
    name = line.split(':')[0]
    value = line.split(': ')[1]
    if value.count(' ') > 0:
        type = 'op'
        monkey1, operation, monkey2 = value.split(' ')
        value = None
    else:
        type = 'num'
        monkey1 = None
        monkey2 = None
        operation = None
    monkeys[name] = monkey(name, type, value, operation, monkey1, monkey2)
    
# monkeys.pop('root')

# zhms should evaluate to 30328243757936


def getHuman(current, shouldEvaluateTo): #Should only be called on a current that hasMonkey.
    if current == getMonkey('humn'):
        print(shouldEvaluateTo)
        quit()
    monkey1Human = getMonkey(current.monkey1).hasHuman()
    monkey2Human = getMonkey(current.monkey2).hasHuman()

    if monkey1Human:
        stable = monkeys[monkey2]
        finding = monkeys[monkey1]
    else:
        stable = monkeys[monkey1]
        finding = monkeys[monkey2]
    
    if current.operation == '+':
        previousYell = shouldEvaluateTo - stable.yell()
    elif current.operation == '*':
        previousYell = shouldEvaluateTo // stable.yell()
    elif current.operation == '-':
        if monkey1Human:
            previousYell = shouldEvaluateTo + stable.yell()
        else:
            previousYell = stable.yell() - shouldEvaluateTo
    elif current.operation == '/':
        if monkey1Human:
            previousYell = shouldEvaluateTo * stable.yell()
        else:
            previousYell = stable.yell() / shouldEvaluateTo


    getHuman(finding, previousYell)

for each in (getMonkey(monkeys['root'].monkey1), getMonkey(monkeys['root'].monkey2)):
    if not each.hasHuman():
        target = each.yell()

getHuman(monkeys['root'], target)