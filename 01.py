with open("01d.txt") as file:
    input = file.read()

elves = input.split("\n\n")
elfCals = []
for elf in elves:
    calories = 0
    for food in elf.split('\n'):
        calories += int(food)
    elfCals.append(calories)
    
elfCals.sort()
print(elfCals[-1] + elfCals[-2] + elfCals[-3])