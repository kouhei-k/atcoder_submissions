N = int(input())
A = [0]*N
xy = [[] for i in range(N)]
for i in range(N):
    A[i] = int(input())
    xy[i] = [tuple(map(int, input().split())) for i in range(A[i])]

ans = 0
for i in range(2**N):
    kind = [False]*N
    for j in range(N):
        if (i >> j) % 2 == 1:
            kind[j] = True

    flag = True
    tmp = 0
    for j in range(N):
        if kind[j]:
            tmp += 1

            for x, y in xy[j]:
                if (y == 1 and kind[x-1]) or (y == 0 and kind[x-1] == False):
                    continue

                else:
                    flag = False
                    tmp = 0
                    break

        if flag == False:
            tmp = 0
            break

    ans = max(ans, tmp)

print(ans)
