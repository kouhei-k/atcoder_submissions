from scipy.sparse.csgraph import floyd_warshall, csgraph_from_dense
H, W = map(int, input().split())
c = [tuple(map(int, input().split())) for i in range(10)]
A = [list(map(int, input().split())) for i in range(H)]
G = csgraph_from_dense(c)
C = floyd_warshall(G)

ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] >= 0:
            ans += int(C[A[i][j]][1])

print(ans)
