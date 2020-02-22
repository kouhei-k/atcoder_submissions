A, B, C, D, E, F = map(int, input().split())

A *= 100
B *= 100
dp = [-1]*(F+1)
if A <= F:
    dp[A] = 0
if B <= F:
    dp[B] = 0
for i in range(A, F + 1):
    if A <= i:
        dp[i] = max(dp[i - A], dp[i])
    if B <= i:
        dp[i] = max(dp[i - B], dp[i])
    if C <= i and dp[i-C] >= 0:
        if dp[i-C] + C <= (i-C - dp[i-C]) * (E / 100):
            dp[i] = max(dp[i-C] + C, dp[i])
    if D <= i and dp[i-D] >= 0:
        if dp[i-D] + D <= (i - D - dp[i-D]) * (E / 100):
            dp[i] = max(dp[i-D] + D, dp[i])


x = 0
id = 0
for i in range(A, F+1):
    if x <= (dp[i] / (i)):
        x = dp[i] / (i)
        id = i
print(id, dp[id])
