def main():
    N = int(input())
    D = [list(map(int, input().split())) for i in range(N)]
    Q = int(input())

    P = [int(input()) for i in range(Q)]

    ans = [0]*(N**2 + 1)

    for i in range(1, N+1):
        for k in range(N+1 - i):
            for j in range(1, N+1):
                for l in range(N+1 - j):
                    S = 0
                    for m in range(k, k+i):
                        S += sum(D[m][l:l+j])
                    ans[i*j] = max(ans[i*j], S)
    M = 0
    for i in range(N*N+1):
        if M > ans[i]:
            ans[i] = M
        else:
            M = ans[i]

    for x in P:
        print(ans[x])


main()
