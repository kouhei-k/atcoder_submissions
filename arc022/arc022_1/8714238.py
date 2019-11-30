from itertools import combinations
S = input()
S = S.upper()
N = len(S)
index = [i for i in range(N)]

for x in combinations(index, 3):
    ret = []
    for y in x:
        ret.append(S[y])
    ret = "".join(ret)
    if ret == "ICT":
        print("YES")
        exit(0)

print("NO")
