import heapq
N, M = map(int, input().split())
lrs = [tuple(map(int, input().split())) for i in range(N)]

s = [0]*(M+1)
S = 0
for l, r, c in lrs:
    l -= 1
    s[l] += c
    s[r] -= c
    S += c
ss = [0]*(M+1)

for i in range(M):
    ss[i+1] = s[i] + ss[i]


print(S - min(ss[1:]))
