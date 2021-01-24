N,K = map(int, input().split())
S = input()
T=[]
import heapq

ans = []
d=dict()
d2=dict()
for x in S:
  heapq.heappush(T,x)
  if x in d:
    d[x]+=1
    d2[x]+=1
  else:
    d[x]=1
    d2[x]=1
c=0

for i in range(N):
  t=[]
  d2[S[i]]-=1

  while(T):
    X=heapq.heappop(T)
    k=0
    if X!=S[i]:
      k+=1
    d[X]-=1
    tmp=0
    for x in d:
      if x in d2 and d2[x] >= d[x]:
        continue
      else:
        if x in d2:
          tmp+= d[x]-d2[x]
        else:
          tmp+=d[x]
    if c+k+tmp <=K:
      c+=k
      ans.append(X)
      for y in t:
        heapq.heappush(T,y)
      break
    else:
      d[X]+=1
      t.append(X)
print(''.join(ans))
