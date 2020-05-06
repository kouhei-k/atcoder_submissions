def main():
    N = int(input())
    a = [list(map(int, input().split())) for i in range(N)]

    def popcount(x):
        # 2bitごとの組に分け、立っているビット数を2bitで表現する
        x = x - ((x >> 1) & 0x5555555555555555)

        # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
        x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

        x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f  # 8bitごと
        x = x + (x >> 8)  # 16bitごと
        x = x + (x >> 16)  # 32bitごと
        x = x + (x >> 32)  # 64bitごと = 全部の合計
        return x & 0x0000007f

    dp = [[0]*(1 << N) for i in range(N+1)]
    dp[0][0] = 1
    mod = 10**9+7
    for j in range(1, 1 << N):
        i = popcount(j)
        DP = dp[i]
        prev = dp[i-1]
        for k in range(N):
            if (j >> k) % 2 == 1:
                if a[i-1][k] == 1:
                    DP[j] += prev[j ^ (1 << k)]
                    DP[j] %= mod

    print(dp[-1][(1 << N) - 1])


main()
