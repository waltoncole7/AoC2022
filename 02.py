# 7 Minutes

with open("02d.txt") as file:
    input = file.read()
rounds = input.split("\n")

total = 0
for round in rounds:
    elf, you = round.split(" ")
    round_score = 0
    if you == "X":
        round_score += 0
        if elf == "A":
            round_score += 3
        elif elf == "B":
            round_score += 1
        else:
            round_score += 2
    elif you == "Y":
        round_score += 3
        if elf == "B":
            round_score += 2
        elif elf == "C":
            round_score += 3
        else:
            round_score += 1
    elif you == "Z":
        round_score += 6
        if elf == "C":
            round_score += 1
        elif elf == "A":
            round_score += 2
        else:
            round_score += 3


    total += round_score
print(total)