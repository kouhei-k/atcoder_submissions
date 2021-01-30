N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(M)]
K = int(input())
CD = [tuple(map(int, input().split())) for i in range(K)]

ans = 0
for i in range(2**K):
    X = [0]*N
    tmp = 0
    for j in range(K):
        if (i >> j) % 2 == 0:
            X[CD[j][0]-1] = 1
        else:
            X[CD[j][1]-1] = 1
    for a, b in AB:
        a -= 1
        b -= 1
        if X[a] and X[b]:
            tmp += 1
    if tmp > ans:
        ans = tmp
print(ans)
