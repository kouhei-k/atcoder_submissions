import sys
sys.setrecursionlimit(10**5)
N=int(input())
a=[int(input()) for i in range(N-1)]
import math
import collections
ans = math.ceil(math.log(N,2))

C=[0]*N
for x in a:
  C[x-1]+=1

depth=[-1]*N
s=set()
d=dict()
d[0]=set()
for i in range(N):

  if C[i] not in d:
    d[C[i]]=set()
  d[C[i]].add(i)

L=[set() for i in range(N)]
for i in range(N-1):
  x = a[i]
  L[x-1].add(i+1)



def dfs(x):
  if depth[x]>=0:
    return(depth[x])
  A=[]
  for y in L[x]:
    A.append(dfs(y))
  A.sort(reverse=True)
  ret=0
  for i in range(len(L[x])):
    if i+A[i]+1>ret:
      ret=i+A[i]+1
  depth[x]=ret
  return(ret)
print(dfs(0))
