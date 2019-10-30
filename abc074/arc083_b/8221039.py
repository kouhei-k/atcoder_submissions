import copy
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
B = copy.deepcopy(A)
table = [[True]*N for i in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if k == i or k == j:
                continue
            else:
                if B[i][k] == B[i][j]+B[j][k]:
                    table[i][k] = False
                B[i][k] = min(B[i][k], B[i][j]+B[j][k])


if A == B:
    for i in range(N):
        for j in range(N):
            if table[i][j]:
                ans += B[i][j]
    print(ans//2)
else:
    print(-1)
