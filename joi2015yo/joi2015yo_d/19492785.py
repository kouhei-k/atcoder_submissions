N, M = map(int, input().split())
D = [int(input()) for i in range(N)]
C = [int(input()) for i in range(M)]

DP = [[0]*(M+1) for i in range(N+1)]
for i in range(N):
    DP[i+1][0] = 10**9


for i in range(N):
    for j in range(M):
        DP[i+1][j+1] = min(DP[i+1][j], DP[i][j] + D[i]*C[j])
print(DP[-1][-1])
