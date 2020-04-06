def main():
    N, T = map(int, input().split())

    AB = [tuple(map(int, input().split())) for i in range(N)]

    AB.sort(key=lambda x: x[0])
    maxA = 0
    for a, b in AB:
        maxA = max(maxA, a)

    dp = [-1]*(T+maxA)
    dp[0] = 0

    for a, b in AB:
        for i in range(T+maxA-1, -1, -1):
            if i >= T:
                if i-a < T and i-a >= 0 and dp[i-a] >= 0:
                    dp[i] = max(dp[i], dp[i-a] + b)

            elif i - a >= 0 and dp[i-a] >= 0:
                dp[i] = max(dp[i], dp[i-a] + b)

    print(max(dp))


main()
