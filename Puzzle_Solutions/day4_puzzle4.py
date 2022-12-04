from getData import *

pairs = getInput(4).split("\n")[:-1]
count = 0
for pair in pairs:
    elf1, elf2 = pair.split(",")
    for i in range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1):
        for j in range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1):
            if (j == i):
                count += 1
                break
        else:
            continue
        break
print(count)
