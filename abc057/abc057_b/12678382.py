N, M = map(int, input().split())

ab = [tuple(map(int, input().split())) for i in range(N)]

cd = [tuple(map(int, input().split())) for j in range(M)]

ans = [0]*N

for i, x in enumerate(ab):
    a, b = x
    D = 10**9
    for j, y in enumerate(cd):
        c, d = y
        dis = abs(a-c) + abs(b-d)
        if dis < D:
            D = dis
            ans[i] = j + 1

print(*ans, sep='
')
