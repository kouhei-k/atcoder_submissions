H,W,D=map(int,input().split())
import collections
import bisect
table=collections.defaultdict(list)
table2=collections.defaultdict(list)
dp=collections.defaultdict(list)
field=[list(map(int,input().split())) for i in range(H)]
for i in range(H):
  for j in range(W):
    table[field[i][j]%D].append((field[i][j],i,j))
    table2[field[i][j]%D].append(field[i][j])
for x in table:
  table[x].sort(key=lambda x:x[0])
  dp[x]=[0]*len(table[x])
  for i in range(1,len(table[x])):
    dp[x][i]=dp[x][i-1]+abs(table[x][i][1]-table[x][i-1][1])+abs(table[x][i][2]-table[x][i-1][2])
  table2[x].sort()
Q=int(input())
LR=[list(map(int,input().split())) for i in range(Q)]
for i in range(Q):
  ans=0
  x,y = LR[i]
  
  id = bisect.bisect_left(table2[x%D],x)
  id2=bisect.bisect_left(table2[x%D],y)
  print(dp[x%D][id2]-dp[x%D][id])
