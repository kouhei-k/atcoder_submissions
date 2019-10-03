S = input()
nwse = [0, 0, 0, 0]

for x in S:
    if x == "N":
        nwse[0] += 1
    elif x == "W":
        nwse[1] += 1
    elif x == "S":
        nwse[2] += 1
    elif x == "E":
        nwse[3] += 1

if nwse[0] > 0 and nwse[2] > 0 or nwse[0] == 0 and nwse[2] == 0:
    if nwse[1] > 0 and nwse[3] > 0 or nwse[1] == 0 and nwse[3] == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
