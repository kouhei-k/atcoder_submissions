N = int(input())
A = [int(input()) for i in range(N)]
B = [[A[i], i+1] for i in range(N)]
B.sort(key=lambda x: x[0])
dp = [1]*N

for i in range(1, N):
    if B[i-1][1] < B[i][1]:
        dp[i] = dp[i-1]+1

ans = N - max(dp)

print(ans)
