def main():
    import sys
    input = sys.stdin.buffer.readline
    N = int(input())
    X = input().decode()
    K = int(X, 2)
    X = list(X)

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

    # X = ['']*N
    # for i in range(N):
    #     X[i] = str(random.randint(0, 1))
    # print("".join(X))
    C = X.count("1")
    dpL = [0]*N
    dpR = [0]*N
    tmp = 1
    dpL[0] = 1 % (C+1)
    L = K % (C+1)

    if C == 1:
        R = 0
    else:
        R = K % (C-1)
        dpR[0] = 1 % (C-1)

    for i in range(1, N):
        dpL[i] = dpL[i-1]*2 % (C+1)
        if C > 1:
            dpR[i] = dpR[i-1]*2 % (C-1)

    dp = [0]*N
    dp[0] = 0
    for i in range(1, N):
        k = i % popcount(i)
        dp[i] = 1 + dp[k]

    # def solve(n, d):

    for i in range(N):
        if X[i] == "0":
            print(dp[(L + dpL[N-i-1]) % (C+1)] + 1)
        else:
            if C == 1:
                print(0)
                continue
            X[i] = '0'
            print(dp[(R - dpR[N-i-1]) % (C-1)] + 1)
            #tmp = dp[int((''.join(X)), 2) % (C-1)] + 1
            X[i] = '1'


main()
# print(dp)
