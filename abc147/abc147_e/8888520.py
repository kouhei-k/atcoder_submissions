
H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
B = [list(map(int, input().split())) for i in range(H)]

C = [[abs(A[i][j] - B[i][j]) for j in range(W)] for i in range(H)]
M = (H+W)*80

dp = [[0 for j in range(W)] for i in range(H)]

for i in range(H):
    for j in range(W):
        if i == 0:
            if j == 0:
                dp[i][j] = (1 << M) << C[i][j]
            else:
                dp[i][j] |= dp[i][j-1] >> C[i][j]
                dp[i][j] |= dp[i][j-1] << C[i][j]

        else:
            if j != 0:
                dp[i][j] |= dp[i][j-1] >> C[i][j]
                dp[i][j] |= dp[i][j-1] << C[i][j]

            dp[i][j] |= dp[i-1][j] >> C[i][j]
            dp[i][j] |= dp[i-1][j] << C[i][j]

dp = bin(dp[i][j])[2:]
dp = dp[::-1]
ans = M
for i, x in enumerate(dp):
    if x == "1":
        ans = min(ans, abs(i - M))

print(ans)
