S=list(input())
N=len(S)
dp=[[0]*13 for i in range(N+1)]
dp[0][0]=1
mod=10**9+7
for i in range(1,N+1):
  for j in range(13):
    if dp[i-1][j]>0:
      if S[i-1]=="?":
        for k in range(10):
          dp[i][(j*10+k)%13]+=dp[i-1][j]
          dp[i][(j*10+k)%13]%=mod
      else:
        dp[i][(j*10+int(S[i-1]))%13]+=dp[i-1][j]
        dp[i][(j*10+int(S[i-1]))%13]%=mod
print(dp[N][5])


         
        
      
    
