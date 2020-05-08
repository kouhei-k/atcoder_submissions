def main():
    S = input()
    N = len(S)
    dp = [[0]*13 for i in range(N+1)]

    mod = 10**9 + 7
    dp[0][0] = 1
    for i, x in enumerate(S):
        for j in range(13):
            if x != '?':
                x = int(x)
                k = j*10 + x
                dp[i+1][k % 13] += dp[i][j]
                dp[i+1][k % 13] %= mod
            else:
                for k in range(10):
                    dp[i+1][(j*10+k) % 13] += dp[i][j]
                    dp[i+1][(j*10+k) % 13] %= mod
    print(dp[-1][5])


main()
