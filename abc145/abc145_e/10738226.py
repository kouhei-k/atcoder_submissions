def main():
    import sys
    input = sys.stdin.readline
    N, T = map(int, input().split())
    ab = [list(map(int, input().split())) for i in range(N)]
    ab.sort(key=lambda x: x[0])
    t = ab[-1][0]
    dp = [-1 for i in range(T+t + 1)]
    dp[0] = 0
    for a, b in ab:
        for i in range(T+t, 0, -1):
            if i >= a:
                if dp[i-a] >= 0 and i - a < T:
                    dp[i] = max(dp[i], dp[i-a] + b)

    for i in range(1, T+t+1):
        dp[i] = max(dp[i], dp[i-1])
    ans = dp[-1]

    # print(dp)
    print(ans)


main()
