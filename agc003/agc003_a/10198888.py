import collections
S = input()

table = collections.defaultdict(int)
for x in S:
    table[x] += 1

N = False
W = False
E = False
S = False

if table["N"] > 0:
    N = True
if table["W"] > 0:
    W = True
if table["E"] > 0:
    E = True
if table["S"] > 0:
    S = True


if (N and S) or ((N or S) == False):
    if (E and W) or ((E or W) == False):
        print("Yes")
        exit(0)
print("No")
