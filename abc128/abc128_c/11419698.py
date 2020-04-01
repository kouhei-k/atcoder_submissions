N, M = map(int, input().split())


K = [[0]*N for i in range(M)]


for i in range(M):
    tmp = list(map(int, input().split()))
    for j in tmp[1:]:
        K[i][j-1] = 1
p = list(map(int, input().split()))
ans = 0
for i in range(2**N):
    tmp = [0]*M
    for j in range(N):
        if (i >> j) % 2 == 1:
            for k in range(M):
                tmp[k] += K[k][j]
    for j in range(M):
        if tmp[j] % 2 != p[j]:
            break
        if j == M-1:
            ans += 1


print(ans)
