#

with open("13d.txt") as file:
    input = file.read()
pairs = input.split('\n\n')

newPairs = []
for pair in pairs:
    newPairs.append(pair.split('\n'))
pairs = newPairs

def order(a, b): #Returns definitive, value
    for i in range(min(len(a), len(b))):
        aType = type(a[i])
        bType = type(b[i])
        if aType == int and bType == int:
            if a[i] != b[i]:
                return (True, a[i] < b[i])
            # return (False, False)
        if bType == int and aType == list:
            b[i] = [b[i]]
        if aType == int and bType == list:
            a[i] = [a[i]]
        aType = type(a[i])
        bType = type(b[i])
        if aType == list and bType == list:
            answer = order(a[i], b[i])
            if answer[0]:
                return answer
    if len(a) != len(b):
        return (True, len(a) < len(b))
    return (False, False)


def listize(rawInput):
    depth = 0
    thisSubList = ''
    thisList = []
    thisNum = ''
    for i in range(1, len(rawInput)):
        char = rawInput[i]
        if char == '[':
            depth += 1
        if depth > 0:
            thisSubList += char
        if depth ==0 and char not in ',]':
            thisNum += char
        if depth == 0 and (char == ',' or char == ']') and thisNum != '':
            thisList.append(int(thisNum))
            thisNum = ''
        if char == ']':
            depth -= 1
            if depth == 0:
                if thisSubList != '':
                    thisList.append(listize(thisSubList))
                thisSubList = ''
    return thisList



i = 1
sum = 0
for pair in pairs:
    term1 = listize(pair[0])
    term2 = listize(pair[1])
    print(term1)
    print(term2)
    print(order(term1, term2))
    if order(term1, term2)[1]:
        sum += i
    i += 1
# print(listize('[1,2,3]'))
# print(listize(pairs[0][0]))
# print('done!')
print(sum)