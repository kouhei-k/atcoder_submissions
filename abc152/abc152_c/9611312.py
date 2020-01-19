import bisect
N = int(input())
P = list(map(int, input().split()))
minP = N+1
ans = 0
for i in range(N):
    if minP >= P[i]:
        ans += 1
    minP = min(minP, P[i])
print(ans)
