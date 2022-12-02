from getData import *

data = getInput(1).split('\n')
elfs = []
elfNum = 0
elfs.append(0)
for x in data:
    if x != "":
        elfs[elfNum] += int(x)
    else:
        elfNum = elfNum + 1
        elfs.append(0)

elfs.sort()
print(elfs[len(elfs)-1])
