from getData import *

pairs = getInput(4).split("\n")[:-1]
count = 0
se = 0
for pair in pairs:
    elf1, elf2 = pair.split(",")
    if (int(elf1.split("-")[0]) <= int(elf2.split("-")[0])):
        if (int(elf1.split("-")[1]) >= int(elf2.split("-")[1])):
            count += 1
        elif (int(elf1.split("-")[0]) == int(elf2.split("-")[0])):
            count += 1

    elif (int(elf1.split("-")[1]) <= int(elf2.split("-")[1])):
        count += 1

print(count)
