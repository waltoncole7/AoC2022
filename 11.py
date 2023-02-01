#

with open("11d.txt") as file:
    input = file.read()
monkeysInput = input.split('\n\n')
# print(monkeysInput)

class monkey():
    def __init__(self, id, items, testDivisor, trueMonkey, falseMonkey, operationString):
        self.id = int(id)
        self.items = [int(item) for item in items]
        self.testDivisor = int(testDivisor)
        self.trueMonkey = int(trueMonkey)
        self.falseMonkey = int(falseMonkey)
        self.operationString = operationString
        self.inspectionCount = 0

    def __str__(self) -> str:
        return str([self.id, self.items, self.testDivisor, self.trueMonkey, self.falseMonkey, self.operationString])

    def inspectAndThrow(self):
        i = 0
        while i < len(self.items):
            item = self.items[i]
            self.inspectionCount += 1
            item = self.operate(item)
            # item = item // 3
            item = item % 9699690
            if item % self.testDivisor == 0:
                self.throw()
                i-= 1
                monkeys[self.trueMonkey].catch(item)
            else:
                self.throw()
                i -= 1
                monkeys[self.falseMonkey].catch(item)
            i += 1
    
    def throw(self): # Throw first item
        self.items.pop(0)
    
    def catch(self, item):
        self.items.append(item)
        
    def operate(self, item):
        terms = self.operationString.split(' ')
        term1 = terms[0]
        operator = terms[1]
        term2 = terms[2]

        if term1 == 'old':
            term1 = item
        else:
            term1 = int(term1)
        if term2 == 'old':
            term2 = item
        else:
            term2 = int(term2)

        if operator == '+':
            return term1 + term2
        elif operator == '*':
            return term1 * term2

monkeys = []
for monkeyInput in monkeysInput:
    monkeyInput = monkeyInput.split('\n')
    monkeys.append(monkey(monkeyInput[0].split('key ')[1][0], monkeyInput[1].split(': ')[1].split(', '), monkeyInput[3].split(' by ')[1], monkeyInput[4].split(' monkey ')[1], monkeyInput[5].split(' monkey ')[1], monkeyInput[2].split('new = ')[1]))

# for monkey in monkeys:
#     print(monkey)

# print(monkeys[2].operate(12))

def round():
    for monkey in monkeys:
        monkey.inspectAndThrow()

for i in range(10000):
    # print('\nAfter Round ' + str(i) + ':')
    # for monkey in monkeys:
    #     print(monkey.items)
    round()

counts = []
for monkey in monkeys:
    counts.append(monkey.inspectionCount)
    
print(counts)
counts.sort()


print(counts[-1] * counts[-2])