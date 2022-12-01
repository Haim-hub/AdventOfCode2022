file = open("Day1/puzzle1.txt")
elfs = []
elfNum = 0
elfs.append(0)
for x in file:
    if x != "\n":
        elfs[elfNum] += int(x)
    else:
        elfNum = elfNum + 1
        elfs.append(0)

elfs.sort()
print(elfs[len(elfs)-1])
