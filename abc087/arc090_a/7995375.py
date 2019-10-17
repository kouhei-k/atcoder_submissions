N=int(input())
A=[list(map(int,input().split()))for i in range(2)]
dp=[[-1]*N for i in range(2)]
dp[0][0]=A[0][0]
for i in range(2):
  for j in range(N):
    if i == 0:
      if j==0:
        continue
      else:
        dp[i][j]=dp[i][j-1]+A[i][j]
    else:
      if j == 0:
        dp[i][j]=dp[i-1][j]+A[i][j]
      else:
        dp[i][j]=A[i][j]+max(dp[i][j-1],dp[i-1][j])
print(dp[1][N-1])
