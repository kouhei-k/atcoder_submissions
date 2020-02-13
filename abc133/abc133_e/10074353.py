import collections
N,K=map(int,input().split())
G=[set() for i in range(N)]
for i in range(N-1):
  a,b=map(int,input().split())
  a-=1
  b-=1
  G[a].add(b)
  G[b].add(a)
m=0
id=9
for i in range(N):
  if len(G[i])>m:
    id=i
    m = len(G[i])
q=collections.deque()
q.append(0)
colored=[False]*N
colored[0]=True
from math import factorial
mod = 10**9 + 7
ans = K
while(q):
  x= q.popleft()
  count=0
  for y in G[x]:
    if colored[y]:
      continue
    else:
      q.append(y)
      colored[y]=True
      count+=1
      
  for i in range(count):
    ans *= K-1-(len(G[x])-count)-i
    ans %= mod
  #print(ans,count,factorial(K-1-(len(G[x])-count)),factorial(count))
print(ans)

  
  
      
  
