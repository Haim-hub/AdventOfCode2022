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

sum = elfs[len(elfs)-1] + elfs[len(elfs)-2] + elfs[len(elfs)-3]
print(sum)
