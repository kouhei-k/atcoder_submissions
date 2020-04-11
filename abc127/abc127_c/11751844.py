N, M = map(int, input().split())
LR = [tuple(map(int, input().split())) for i in range(M)]

l = 1
r = N
for i in range(M):
    l = max(l, LR[i][0])
    r = min(r, LR[i][1])

ans = max(0, r - l + 1)
print(ans)
