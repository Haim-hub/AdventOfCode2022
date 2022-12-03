import string
from getData import *

rucksacks = getInput(3).split("\n")[:-1]

priorities = list(string.ascii_letters)
score = 0


def getPrioriti(letter):
    return priorities.index(letter)+1


for rucksack in rucksacks:
    compartment1, compartment2 = rucksack[:len(
        rucksack)//2], rucksack[len(rucksack)//2:]
    for item in compartment1:
        if item in compartment2:
            score += getPrioriti(item)
            break

print(score)
