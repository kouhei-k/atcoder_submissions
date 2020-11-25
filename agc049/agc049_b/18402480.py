N=int(input())
S=list(input())
G=list(input())
ans=0

import collections
q=collections.deque()
for i in range(N):
  if S[i]=='1':
    q.append(i)
ans=0
for i in range(N):
  if S[i]!=G[i]:
    while(q and q[0]<=i):
      q.popleft()
    
    if q:
      x=q.popleft()
      S[x]='0'

      ans+=x-i
    else:
      print(-1)
      exit(0)
      
   
print(ans)
