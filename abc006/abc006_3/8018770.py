N, M = map(int, input().split())
if M < 2 * N or M > 4*N:
    print(-1, -1, -1)
else:
    if M == 2*N:
        print(N, 0, 0)
    elif M == 3*N:
        print(0, N, 0)
    elif M == 4*N:
        print(0, 0, N)
    else:
        k = M - 2*N
        c = k // 2
        if k % 2 == 1:
            print(N - 1 - c, 1, c)
        else:
            print(N-c, 0, c)
