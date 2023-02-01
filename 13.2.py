#
from copy import deepcopy

with open("13d.txt") as file:
    input = file.read()
lines = input.split('\n')
for line in lines:
    if line == '':
        lines.remove(line)
# print(lines)

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

listLines = [[[2]], [[6]]]
for line in lines:
    listLines.append(listize(line))
# print(listLines)

for i in range(1, len(listLines)):
    # print(listLines[:5])
    moving = listLines[i]
    j=i-1
    while j >= 0 and order(deepcopy(moving), deepcopy(listLines[j]))[1]:
        # print(i, j, moving, listLines[j])
        listLines[j+1] = listLines[j]
        j-=1
    listLines[j+1] = moving
print((listLines.index([[2]]) + 1) * (listLines.index([[6]]) + 1))
    
# print(listLines)
# print((listLines.index([[2]])+1),(1+listLines.index([[6]])))


# def merge(list1, list2):
#     list2Index = 0
#     print('working')
#     for item1 in list1:
#         while list2Index < len(list2):
#         for item2 in list2:
#             if order(item1, list2[list2Index]):
#                 list2.insert(list2Index, item1)
#     return list2

# def mergeSort(workingList, depth):
#     print(depth)
#     if len(workingList) < 2:
#         return workingList
#     return merge(mergeSort(workingList[:len(workingList) // 2], depth + 1) ,mergeSort(workingList[len(workingList) // 2:], depth + 1))


# print(merge([1, 3, 5], [2, 4, 6]))
# answer = mergeSort(listLines, 0)
# print('done')
# print(answer.index([[2]])*answer.index([[6]]))
