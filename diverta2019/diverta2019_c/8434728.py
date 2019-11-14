N = int(input())
s = [input() for i in range(N)]
minAB = 0
AB = [0, 0]
count = 0
for i, x in enumerate(s):
    minAB += x.count("AB")
    if x[-1] == "A":
        AB[0] += 1
    if x[0] == "B":
        AB[1] += 1
        if x[-1] == "A":
            count += 1
if count != max(AB) or count == 0:
    print(minAB + min(AB))
else:
    print(minAB + min(AB)-1)
