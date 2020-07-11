N, M = map(int, input().split())
xy = [tuple(map(int, input().split())) for i in range(M)]

G = [set() for i in range(N)]
for x, y in xy:
    x -= 1
    y -= 1
    G[y].add(x)

dp = [0]*(1 << N)
dp[0] = 1
for i in range(1, 1 << N):
    s = set()
    for j in range(N):
        if (i >> j) % 2 == 1:
            s.add(j)
    for x in s:
        if len(G[x] & s):
            continue
        else:
            dp[i] += dp[i - (1 << x)]


print(dp[-1])
