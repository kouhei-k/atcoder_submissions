N=int(input())
S=input()
ans=0

def LCS(s1,s2):
  dp = [[0]*(len(s2)+1) for i in range(len(s1)+1)]
  ret = 0
  for i in range(len(s1)):
    for j in range(len(s2)):
      tmp = dp[i][j]
      if s1[i] == s2[j]:
        tmp += 1
      dp[i+1][j+1] = max(tmp, dp[i+1][j], dp[i][j+1])
      ret = max(ret, dp[i+1][j+1])
  return(ret)
ans = min(N - 2*LCS(S[:i],S[i:]) for i in range(N))
print(ans)
