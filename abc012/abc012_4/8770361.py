from scipy.sparse.csgraph import csgraph_from_dense,dijkstra
N,M=map(int,input().split())
g=[[10**9]*N for i in range(N)]
for i in range(M):
  a,b,t=map(int,input().split())
  a-=1
  b-=1
  g[a][b]=t
  g[b][a]=t
g =csgraph_from_dense(g,null_value=10**9)
G=dijkstra(g)
ans=10**9
id=0
for i in range(N):
  if ans > max(G[i]):
    ans=max(G[i])
print(int(ans))
