def main():
    import sys
    input = sys.stdin.buffer.readline
    N = int(input())
    D = [list(map(int, input().split())) for i in range(N)]
    Q = int(input())
    P = [int(input()) for i in range(Q)]

    DP = [0] * (N**2 + 1)

    S = [[0]*(N+1) for i in range(N+1)]
    for i in range(N):
        for j in range(N):
            S[i+1][j+1] = S[i+1][j] + S[i][j+1] - S[i][j] + D[i][j]

    for i in range(N):
        for j in range(N):
            for i2 in range(i+1, N+1):
                for j2 in range(j+1, N+1):
                    s = (i2-i)*(j2-j)
                    point = S[i2][j2] - S[i][j2] - S[i2][j] + S[i][j]
                    if point > DP[s]:
                        DP[s] = point

    for i in range(Q):
        print(max(DP[:P[i]+1]))


main()
