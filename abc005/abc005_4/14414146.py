def main():
    N = int(input())
    D = [list(map(int, input().split())) for i in range(N)]
    DT = [[D[i][j] for i in range(N)] for j in range(N)]
    Q = int(input())

    P = [int(input()) for i in range(Q)]

    ans = [0]*(N*N+1)
    for i in range(1, N+1):
        for j in range(1, N+1):
            id = i*j  # 面積
            S1 = 0
            for k in range(i):
                S1 += sum(D[k][:j])
            for k in range(N+1-i):

                if k > 0:
                    S1 -= sum(D[k-1][:j])
                    S1 += sum(D[k+i-1][:j])
                S = S1
                for l in range(N+1-j):
                    if l > 0:
                        S -= sum(DT[l-1][k:k+i])
                        S += sum(DT[l+j-1][k:k+i])
                    if S > ans[id]:
                        ans[id] = S

    M = 0
    for i in range(N*N+1):
        if M > ans[i]:
            ans[i] = M
        else:
            M = ans[i]

    for q in P:
        print(ans[q])


main()
