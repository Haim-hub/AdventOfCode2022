from getData import *

data = getInput(2).split("\n")
score = 0
for x in data[:-1]:
    hands = x.split()
    print(x)
    if hands[1] == "Y":  # draw
        score += 3
        if hands[0] == "A":  # rock
            score += 1
        elif hands[0] == "B":  # paper
            score += 2
        elif hands[0] == "C":  # scissor
            score += 3

    elif hands[1] == "Z":  # win
        score += 6
        if hands[0] == "A":  # rock
            score += 2
        elif hands[0] == "B":  # paper
            score += 3
        elif hands[0] == "C":  # scissor
            score += 1

    elif hands[1] == "X":  # lose
        score += 0
        if hands[0] == "A":  # rock
            score += 3
        elif hands[0] == "B":  # paper
            score += 1
        elif hands[0] == "C":  # scissor
            score += 2


print(score)
