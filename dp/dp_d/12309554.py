def main():
    import sys
    input = sys.stdin.readline
    N, W = map(int, input().split())
    wv = [tuple(map(int, input().split())) for i in range(N)]

    dp = [-1]*(W+1)
    dp[0] = 0
    for w, v in wv:
        for j in range(W-w, -1, -1):
            if dp[j] >= 0 and dp[j+w] < dp[j]+v:
                dp[j+w] = dp[j] + v

    print(max(dp))


main()
