import collections
import sys
sys.setrecursionlimit(10**5)
N, M = map(int, input().split())
G = [set() for i in range(N)]
L = [-1]*N


def solve(x, r):
    if L[x] >= 0:
        return(L[x])
    res = 0
    for z in G[x]:
        if r[z]:
            r[z] = False
            res = max(res, solve(z, r) + 1)
        else:
            res = max(res, L[z]+1)
    L[x] = res
    return(res)


for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    G[x].add(y)

r = [True]*N

for i in range(N):
    # print(L)
    if r[i]:
        L[i] = solve(i, r)
print(max(L))

# print(L)
