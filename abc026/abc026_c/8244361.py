import collections
import sys
sys.setrecursionlimit(10000)
N=int(input())
B=[int(input()) for i in range(N-1)]
table=collections.defaultdict(list)

def solve(key):
  if dp[key]!=-1:
    return(dp[key])
  tmp = table[key]
  ans=[0,10**7]
  for x in tmp:
    res=solve(x)
    ans[0]=max(ans[0],res)
    ans[1]=min(ans[1],res)
  dp[key]= sum(ans)+1
  return(dp[key])

for i in range(N-1):
  table[B[i]-1].append(i+1)
  
dp=[-1]*N
tmp = table.keys()
for i in range(N):
  if i not in tmp:
    dp[i]=1

print(solve(0))
