import collections
import bisect
N = int(input())
S = list(input())

dp = [[0]*10 for i in range(N)]


table = collections.defaultdict(list)


for i in range(N):
    table[int(S[i])].append(i)

ans = 0
for x in range(10):
    if x not in table:
        continue
    i = table[x][0]
    for y in range(10):
        if y not in table:
            continue
        idy = bisect.bisect_left(table[y], i + 1)
        if idy < len(table[y]):
            idy = table[y][idy]
            for z in range(10):
                if z not in table:
                    continue
                idz = bisect.bisect_left(table[z], idy+1)
                if idz < len(table[z]):
                    ans += 1
print(ans)
