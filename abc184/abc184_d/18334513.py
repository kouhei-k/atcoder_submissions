A, B, C = map(int, input().split())

D = [[[0] * 101 for i in range(101)] for j in range(101)]

tmp = [A, B, C]
tmp.sort()
A = tmp[-1]
B = tmp[1]
C = tmp[0]

D[A][B][C] = 1

ans = 0

for i in range(A, 100):
    for j in range(B, 100):
        for k in range(C, 100):
            if i != A or j != B or k != C:
                if D[i-1][j][k] > 0:
                    D[i][j][k] += D[i-1][j][k] * (i-1) / (i+j+k - 1)
                if D[i][j-1][k] > 0:
                    D[i][j][k] += D[i][j-1][k] * (j-1) / (i+j+k - 1)
                if D[i][j][k-1] > 0:
                    D[i][j][k] += D[i][j][k-1] * (k-1) / (i+j+k - 1)
                # D[i][j][k] = (D[i-1][j][k]*(i-1) + D[i][j-1][k] *
                #               (j-1)+D[i][j][k-1]*(k-1)) / (i+j+k-1)
                # print(i, j, k, D[i-1][j][k]*(i-1), D[i][j-1][k] *
                #       (j-1), D[i][j][k-1]*(k-1), D[i][j][k])
                ans += D[i][j][k]
# for i in range(99):
#     for j in range(99):
#         if D[99][i][j] > 0:
#             ans += (99+i+j) / (i+j + 99)
#         if D[i][99][j] > 0:
#             ans += (99+i+j) / (i+j + 99)
#         if D[i][j][99] > 0:
#             ans += (99+i+j) / (i+j + 99)
#         # ans += D[100][i][j]
#         # ans += D[i][100][j]
#         # ans += D[i][j][100]

print(ans+1)
