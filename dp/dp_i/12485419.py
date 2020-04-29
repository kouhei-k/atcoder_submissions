def main():
    N = int(input())
    p = tuple(map(float, input().split()))

    dp = [0 for i in range(N+1)]
    # iまで見たときに表の枚数がj枚の確率

    dp[0] = 1 - p[0]
    dp[1] = p[0]
    for i in range(1, N):
        for j in range(i+1, -1, -1):

            dp[j] = dp[j]*(1-p[i]) + dp[j-1]*p[i]
            # else:
            #     dp[j] = dp[j]*(1-p[i])

    ans = sum(dp[N//2 + 1:])
    print(ans)


main()
