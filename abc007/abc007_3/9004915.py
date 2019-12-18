import collections
R,C=map(int,input().split())
s=list(map(int,input().split()))
g=list(map(int,input().split()))
field=[list(input()) for i in range(R)]
q=collections.deque()
s[0],s[1],g[0],g[1]=s[0]-1,s[1]-1,g[0]-1,g[1]-1
q.append(s)
dp=[[-1]*C for i in range(R)]
dp[s[0]][s[1]]=0
while(q):
  r,c=q.popleft()
  if r==g[0] and c==g[1]:
    print(dp[r][c])
    break
  else:
    if r>0 and field[r-1][c]!="#" and dp[r-1][c] == -1:
      dp[r-1][c]=dp[r][c]+1
      q.append((r-1,c))
    if r<R-1 and field[r+1][c]!="#" and dp[r+1][c] == -1:
      dp[r+1][c]=dp[r][c]+1
      q.append((r+1,c))
    if c>0 and field[r][c-1]!="#" and dp[r][c-1] == -1:
      dp[r][c-1]=dp[r][c]+1
      q.append((r,c-1))
    if c<C-1 and field[r][c+1]!="#" and dp[r][c+1] == -1:
      dp[r][c+1]=dp[r][c]+1
      q.append((r,c+1))
