N, K = map(int, input().split())
T = [int(input()) for i in range(N)]
if K >= N:
    print(N)
else:
    T.sort()
    D = [T[i+1] - T[i] - 1 for i in range(N-1)]

    k = N - K
    D.sort()
    print(N + sum(D[:k]))
