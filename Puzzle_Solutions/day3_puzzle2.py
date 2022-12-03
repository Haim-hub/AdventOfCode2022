import string
from getData import *

rucksacks = getInput(3).split("\n")[:-1]

groupSize = 3
groups = [
    rucksacks[idx:idx+groupSize] for idx in range(0, len(rucksacks), groupSize)
]

priorities = list(string.ascii_letters)
score = 0


def getPrioriti(letter):
    return priorities.index(letter)+1


for group in groups:
    for item in group[0]:
        if item in group[1]:
            if item in group[2]:
                score += getPrioriti(item)
                break

print(score)
