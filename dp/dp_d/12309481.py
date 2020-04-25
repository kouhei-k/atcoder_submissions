def main():
    N, W = map(int, input().split())
    wv = [tuple(map(int, input().split())) for i in range(N)]

    dp = [-1]*(W+1)
    dp[0] = 0
    for w, v in wv:
        for j in range(W-1, -1, -1):
            if dp[j] >= 0 and j+w <= W:
                dp[j+w] = max(dp[j+w], dp[j] + v)

    print(max(dp))


main()
