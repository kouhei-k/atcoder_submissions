def main():

    import sys
    input = sys.stdin.buffer.readline
    N, K = map(int, input().split())
    LR = [tuple(map(int, input().split())) for i in range(K)]
    LR.sort()
    S = [0]*(N)
    S[0] = 1
    mod = 998244353
    for i in range(N-1):
        S[i] += S[i-1]
        s = S[i]
        for L, R in LR:
            if i+L < N:
                S[i+L] += s
                S[i+L] %= mod
            if i + R + 1 < N:
                S[i+R+1] -= s
                S[i+R+1] %= mod
    # print(S)
    print(S[-1])


main()
