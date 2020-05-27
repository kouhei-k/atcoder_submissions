def main():
  W=int(input())
  N,K=map(int,input().split())
  AB=[list(map(int,input().split())) for i in range(N)]

  dp=[[-1,0] for i in range(W+1)]
  dp[0][0]=0
  ans=0
  AB.sort(key=lambda x:x[1],reverse=True)
  for A,B in AB:
    for j in range(W-1,-1,-1):
      if j+A <= W and dp[j][0] >= 0 and dp[j][1]<K:
        if dp[j+A][0]<0:
          dp[j+A][0]=dp[j][0]+B
          dp[j+A][1]=dp[j][1]+1
        else:
        
          if dp[j+A][0] < dp[j][0]+B:
            dp[j+A][0]=dp[j][0]+B
            dp[j+A][1]=dp[j][1]+1
          elif dp[j+A][0]==dp[j][0]+B:
            dp[j+A][1]=min(dp[j][1]+1,dp[j+A][1])
          
        ans=max(ans,dp[j+A][0])
  print(ans)
main()
