from getData import *

data = getInput(2).split("\n")
score = 0
for x in data[:-1]:
    hands = x.split()
    print(x)
    if hands[1] == "Y":
        score += 2
    elif hands[1] == "Z":
        score += 3
    elif hands[1] == "X":
        score += 1

    if x == "A Y":  # rock vs. paper
        score += 6
    elif x == "B Z":  # paper vs. scissor
        score += 6
    elif x == "C X":  # scissor vs. rock
        score += 6
    elif x == "A X":  # rock vs. rock
        score += 3
    elif x == "B Y":  # paper vs. paper
        score += 3
    elif x == "C Z":  # scissor vs. scissor
        score += 3


print(score)
