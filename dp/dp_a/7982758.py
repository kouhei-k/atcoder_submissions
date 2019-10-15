N = int(input())

h = list(map(int, input().split()))

dp = [-1]*N


def solve(id):
    if dp[id] == -1:
        if id == 0:
            dp[id] = 0
        elif id == 1:
            dp[id] = abs(h[1]-h[0])
        else:
            dp[id] = min(dp[id-1] + abs(h[id] - h[id-1]),
                         dp[id-2] + abs(h[id] - h[id-2]))
    return dp[id]


for i in range(N):
    solve(i)

print(dp[-1])
