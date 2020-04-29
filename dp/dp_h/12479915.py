H, W = map(int, input().split())
a = [list(input()) for i in range(H)]

dp = [[0]*W for i in range(H)]
mod = 10**9 + 7
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if a[i][j] == '#':
            continue
        if j > 0:
            dp[i][j] += dp[i][j-1]
        if i > 0:
            dp[i][j] += dp[i-1][j]
        dp[i][j] %= mod
print(dp[-1][-1])
