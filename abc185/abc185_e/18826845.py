N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = A
b = B
if N < M:
  a = B
  b = A
  N,M = M,N

dp = [[N+M]*(M+1) for i in range(N+1)]
dp[0][0] = 0
for i in range(N+1):
  for j in range(M+1):
    ret = 0
    # A[i] to B[j] ga ittisurunara, dp[i][j] = dp[i-1][j-1]
    # A[i]tpoB[j]gaittisinainara,dp[i][j] = dp[i-1][j-1] + 1
    if i == 0:
      dp[i][j] = j
    elif j == 0:
      dp[i][j] = i
    else:
      if a[i-1] == b[j-1]:
        dp[i][j] = min(dp[i-1][j-1], dp[i][j-1] + 1, dp[i-1][j] + 1)
      else:
        dp[i][j] = min(dp[i-1][j-1] + 1, dp[i][j-1] + 1, dp[i-1][j] +1)
print(dp[-1][-1])
