
def main():
    H, N = map(int, input().split())
    AB = [tuple(map(int, input().split())) for i in range(N)]

    dp = [-1]*(H+1)
    dp[H] = 0

    for i in range(H, 0, -1):
        for a, b in AB:

            if dp[i] >= 0:
                next = max(i-a, 0)
                if dp[next] < 0:
                    dp[next] = dp[i] + b
                else:
                    if dp[next] > dp[i] + b:
                        dp[next] = dp[i] + b

    print(dp[0])
main()
