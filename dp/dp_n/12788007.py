def main():
    N = int(input())
    a = list(map(int, input().split()))
    inf = 10 ** 13
    dp = [[0]*N for i in range(N)]
    s = [0]*(N+1)
    for i, x in enumerate(a):
        s[i+1] = s[i]+a[i]
        dp[i][i] = 0
    for i in range(N-2, -1, -1):
        DP = dp[i]
        si = s[i]
        for j in range(i+1, N):
            tmp = s[j+1] - si
            D = inf
            for k in range(i, j):
                cost = DP[k]+dp[k+1][j]
                if D > cost:
                    D = cost
            DP[j] = D + tmp
    print(dp[0][N-1])
main()
