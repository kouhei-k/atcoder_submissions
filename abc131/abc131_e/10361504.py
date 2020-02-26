N, K = map(int, input().split())

k = (N-1)*(N-2) // 2
if k < K:
    print(-1)
else:
    d = k - K
    M = N-1 + d
    print(M)

    for i in range(N-1):
        print(i+1, N)

    count = 0

    flag = True
    if d > 0:
        for i in range(N-2):
            for j in range(i+1, N-1):
                print(i+1, j+1)
                count += 1
                if count == d:
                    flag = False
                    break
            if flag:
                continue
            else:
                break
