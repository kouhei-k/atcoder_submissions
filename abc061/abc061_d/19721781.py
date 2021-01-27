import collections

N,M=map(int,input().split())
G=[set() for i in range(N)]
for i in range(M):
  a,b,c = map(int,input().split())
  a-=1
  b-=1
  G[b].add((a,c))


S=set()
q=collections.deque()
S.add(N-1)
q.append(N-1)
while(q):
  x = q.popleft()
  for y,_ in G[x]:
    if y in S:
      continue
    else:
      S.add(y)
      q.append(y)

X=len(S)

G2=[set() for i in range(N)]
for i in range(N):
  if i not in S:
    continue
  for y,c in G[i]:
    if y not in S:
      continue
    G2[y].add((i,-c))

import heapq
D=[float('inf')]*N
hq=[(0,0)]
D[0]=0
count=0
flag=False
while(hq):
  if count>X:
    flag=True
    break
  count+=1
  c,x=heapq.heappop(hq)
  for y,c2 in G2[x]:
    if D[y]>c+c2:
      D[y]=c+c2
      heapq.heappush(hq,(c+c2,y))
if flag:
  print('inf')
else:
  print(-D[-1])
