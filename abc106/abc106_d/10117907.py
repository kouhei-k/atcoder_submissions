import collections
import heapq
import bisect
import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
LR = [tuple(map(int, input().split())) for i in range(M)]
LR.sort(key=lambda x: x[1])
table = collections.defaultdict(list)
for l, r in LR:
    table[l].append(r)

ss = [[0]*(N+1) for i in range(N+1)]
s = [[0]*(N+1) for i in range(N+1)]
for i in range(1, N+1):
    for x in table[i]:
        ss[i][x] += 1
    for j in range(i, N+1):
        s[i][j] = s[i][j-1] + ss[i][j]


for i in range(Q):
    p, q = map(int, input().split())
    ret = 0
    for j in range(p, q+1):
        ret += s[j][q]
    print(ret)
