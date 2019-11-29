N=int(input())
abc=[tuple(map(int,input().split())) for i in range(N-1)]
g=[set() for i in range(N)]
for a,b,c in abc:
  g[a-1].add((b-1,c))
  g[b-1].add((a-1,c))
memo=[-1]*N

Q,K=map(int,input().split())
import collections
q=collections.deque([(K-1,0)])
memo[K-1]=0
while(q):
  
  x,w = q.popleft()
  for a,b in g[x]:
    if memo[a]==-1:
      memo[a]=w+b
      q.append((a,w+b))
  
for i in range(Q):
  x,y=map(int,input().split())
  print(memo[x-1]+memo[y-1])
