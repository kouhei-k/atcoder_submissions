
N = int(input())
XYZ = [list(map(int, input().split())) for i in range(N)]
ans = 0
D = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        cost = 0
        cost += abs(XYZ[i][0] - XYZ[j][0])
        cost += abs(XYZ[i][1] - XYZ[j][1])
        cost += max(XYZ[j][2] - XYZ[i][2], 0)
        D[i][j] = cost


C = [[10**15]*N for i in range(2**N)]
C[2**N-1][0] = 0
for i in range((1 << N) - 2, -1, -1):
    for j in range(N):
        for k in range(N):
            if (i >> k) % 2 == 0:
                C[i][j] = min(C[i][j], C[i | 1 << k][k] + D[j][k])
print(C[0][0])
