N = int(input())
F = [list(map(int, input().split())) for i in range(N)]
P = [list(map(int, input().split())) for i in range(N)]

ans = - (10**7)*N
for i in range(1, 2**10):
    tmp = 0
    for j in range(N):
        count = 0
        for k in range(10):
            if F[j][k] == 1 and (i >> k) % 2 == 1:
                count += 1
        tmp += P[j][count]

    ans = max(ans, tmp)

print(ans)
