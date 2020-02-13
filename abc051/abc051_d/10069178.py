from scipy.sparse.csgraph import shortest_path
import numpy as np
N,M=map(int,input().split())
abc = [tuple(map(int,input().split())) for i in range(M)]
g = [[10**9]*N for i in range(N)]
for a,b,c in abc:
  a,b = a-1,b-1
  g[a][b]=c
  g[b][a]=c
g = np.array(g)
G,P=shortest_path(g,return_predecessors=True)
ans=set()
for i in range(N):
  for j in range(N):
    if P[i][j]>0 and (P[i][j],j) not in ans:
      ans.add((j,P[i][j]))

print(M-len(ans))
