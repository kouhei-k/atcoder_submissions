H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
S = 0
m = 100
for i in range(H):
    for j in range(W):
        if A[i][j] < m:
            m = A[i][j]
        S += A[i][j]
print(S - m*H*W)
