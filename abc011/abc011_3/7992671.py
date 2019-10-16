N = int(input())
NG = [int(input()) for i in range(3)]

dp = [[False, -1] for i in range((N+1))]
if N not in NG:
    dp[N] = [True, 0]

for i in reversed(range(N)):
    if i not in NG:
        for j in range(1, 4):
            if i + j <= N and dp[i+j][0]:
                if dp[i][0]:
                    dp[i][1] = min(dp[i][1], dp[i+j][1] + 1)
                else:
                    dp[i][0] = True
                    dp[i][1] = dp[i+j][1] + 1

    else:
        dp[i][0] = False

if dp[0][0] and dp[0][1] <= 100:
    print("YES")

else:
    print("NO")
