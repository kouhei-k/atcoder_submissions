def main():
    import sys
    input = sys.stdin.readline
    N, W = map(int, input().split())
    wv = [tuple(map(int, input().split())) for i in range(N)]

    dp = [-1]*(10**3 * N + 1)
    dp[0] = 0
    ans = 0
    for w, v in wv:
        for j in range((10**3 * N) - v, -1, -1):
            if dp[j] >= 0 and dp[j] + w <= W:
                if dp[j+v] < 0 or dp[j+v] > dp[j] + w:
                    dp[j+v] = dp[j] + w
                if ans < j+v:
                    ans = j+v
    print(ans)


main()
