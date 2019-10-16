N = int(input())
a = list(map(int, input().split()))

dp = [-1]*N
for i in range(N):
    if i == 0:
        dp[i] = 0
    elif i == 1:
        dp[i] = abs(a[1] - a[0])
    else:
        dp[i] = min(dp[i-2] + abs(a[i] - a[i-2]), dp[i-1] + abs(a[i] - a[i-1]))

print(dp[N-1])
