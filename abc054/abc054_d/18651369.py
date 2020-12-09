N,Ma,Mb=map(int,input().split())
abc= [tuple(map(int,input().split())) for i in range(N)]
dp=[[-1]*500 for i in range(500)]
dp[0][0]=0
for a,b,c in abc:
  for i in range(499,-1,-1):
    for j in range(499,-1,-1):
      if dp[i][j]>=0:
        if dp[i+a][j+b]>=0:
          dp[i+a][j+b]=min(dp[i+a][j+b],dp[i][j]+c)
        else:
          dp[i+a][j+b]=dp[i][j]+c
ans=-1
for i in range(1,500):
  for j in range(1,500):
    if dp[i][j]>0 and i*Mb==Ma*j:
      if ans==-1:
        ans=dp[i][j]
      else:
        if dp[i][j]<ans:
          ans=dp[i][j]
print(ans)
