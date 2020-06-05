H,W=map(int,input().split())
S=[input()+"#" for i in range(H)]
S.append("#"*(W+1))



dp=[[-1]*(W+1) for i in range(H+1)]

for i in range(H):
  for j in range(W):
    if S[i][j+1]=="#" and S[i+1][j+1]=="#" and S[i+1][j]=='#':
      dp[i][j] = 0
for i in range(H-1,-1,-1):
    for j in range(W-1,-1,-1):
        if dp[i][j] >= 0:
            continue
        else:
            if(S[i+1][j] == '.' and dp[i+1][j] == 0) or (S[i][j+1]=='.' and dp[i][j+1] == 0) or (S[i+1][j+1] == '.' and dp[i+1][j+1] == 0):
                dp[i][j] = 1
            else:
                dp[i][j] = 0
#print(*dp,sep='
')
ans = ['Second','First']
print(ans[dp[0][0]])
          
