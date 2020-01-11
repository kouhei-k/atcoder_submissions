import collections
N, C = map(int, input().split())
D = [tuple(map(int, input().split())) for i in range(C)]
c = [list(map(int, input().split())) for i in range(N)]

table = [collections.defaultdict(int) for i in range(3)]

for i in range(N):
    for j in range(N):
        k = (i+j) % 3
        table[k][c[i][j] - 1] += 1


ans = 10**9
for i in range(C):
    tmp = 0
    for x in table[0]:
        tmp += D[x][i]*table[0][x]

    for j in range(C):
        if i == j:
            continue
        tmp2 = 0
        for x in table[1]:
            tmp2 += D[x][j]*table[1][x]
        for k in range(C):
            if i == k or j == k:
                continue
            tmp3 = 0
            for x in table[2]:
                tmp3 += D[x][k]*table[2][x]

            ans = min(ans, tmp+tmp2+tmp3)
print(ans)
