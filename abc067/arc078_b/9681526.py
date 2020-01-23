N=int(input())
import collections
import heapq
ab=[tuple(map(int,input().split())) for i in range(N-1)]
G=[set() for i in range(N)]
for a,b in ab:
  a-=1
  b-=1
  G[a].add(b)
  G[b].add(a)
q=collections.deque()

dis=[[-1]*N for i in range(2)]
dis[0][0]=0
q.append(0)
while(q):
  x=q.popleft()
  for y in G[x]:
    if dis[0][y]==-1:
      q.append(y)
      dis[0][y]=dis[0][x]+1
dis[1][N-1]=0
q.append(N-1)
while(q):
  x=q.popleft()
  for y in G[x]:
    if dis[1][y]==-1:
      q.append(y)
      dis[1][y]=dis[1][x]+1

hqF=[(0,0)]
hqS=[(0,N-1)]
colord=[False]*N

while(1):
  if len(hqF)==0:
    print("Snuke")
    exit(0)
  _,x = heapq.heappop(hqF)
  while(colord[x]):
    if hqF:
      _,x = heapq.heappop(hqF)
    else:
      print("Snuke")
      exit(0)
  colord[x]=True
  for y in G[x]:
    if colord[y]==False:
      heapq.heappush(hqF,(dis[1][y],y))

  if len(hqS)==0:
    print("Fennec")
    exit(0)
  _,x = heapq.heappop(hqS)
  while(colord[x]):
    if hqF:
      _,x = heapq.heappop(hqS)
    else:
      print("Fennec")
      exit(0)
  colord[x]=True
  for y in G[x]:
    if colord[y]==False:
      heapq.heappush(hqS,(dis[0][y],y))
