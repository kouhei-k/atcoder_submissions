from itertools import permutations
from scipy.sparse.csgraph import dijkstra, csgraph_from_dense
N, M, R = map(int, input().split())
t = set(map(int, input().split()))
ABC = [map(int, input().split()) for i in range(M)]

root = [[10**9]*N for i in range(N)]
for a, b, c in ABC:
    root[a-1][b-1] = c
    root[b-1][a-1] = c
g = csgraph_from_dense(root, null_value=10**9)
G = dijkstra(g)
ans = 10**9
for l in permutations(t):
    tmp = 0
    for i in range(1, R):
        tmp += min(root[l[i-1]-1][l[i]-1], G[l[i-1]-1][l[i]-1])
    ans = min(tmp, ans)
print(int(ans))
