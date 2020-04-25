N = int(input())
abc = [tuple(map(int, input().split())) for i in range(N)]

dp = [[-1]*3 for i in range(N)]

dp[0][0] = abc[0][0]
dp[0][1] = abc[0][1]
dp[0][2] = abc[0][2]

for i in range(1, N):
    for j in range(3):
        dp[i][j] = max(dp[i-1][(j+1) % 3], dp[i-1][(j+2) % 3]) + abc[i][j]
print(max(dp[-1]))
