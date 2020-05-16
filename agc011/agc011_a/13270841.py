N, C, K = map(int, input().split())
T = [int(input()) for i in range(N)]
T.sort()
prev = -1
r = 0
ans = 0
for t in T:
    if prev > 0 and t - prev > K:
        prev = t
        r = 1
        ans += 1
    elif prev < 0:
        prev = t
        ans += 1
        r = 1
    else:
        r += 1

    if r == C:
        prev = -1
        r = 0


print(ans)
