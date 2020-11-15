def main():
    import sys
    input = sys.stdin.readline
    H, W = map(int, input().split())
    S = [input() for i in range(H)]

    DP = [[0]*W for i in range(H)]

    DP[0][0] = 1
    mod = 10**9 + 7

    A = [0]*W
    C = [0]*(H+W)
    for i in range(H):
        B = 0
        for j in range(W):
            if i == 0:
                tmp = 0
                if j == 0:
                    B = 1
                    A[0] = 1
                    C[j-i + H-1] = 1
                else:
                    if S[i][j] == '.':
                        DP[i][j] = B
                        B *= 2
                        B %= mod
                        A[j] += DP[i][j]
                        C[j-i + H-1] += DP[i][j]
                    else:
                        break
            else:
                ret = 0

                if S[i][j] == '.':
                    if j == 0:
                        ret += A[j]
                    else:
                        ret += A[j]
                        ret += B
                        if i > 0:
                            ret += C[j-i+H-1]
                    ret %= mod
                    # print(i, j, A[j], B, C[j-i+H-1], ret)
                    A[j] += ret
                    A[j] %= mod
                    B += ret
                    B %= mod
                    C[j-i + H - 1] += ret
                    C[j-i+H-1] %= mod
                    DP[i][j] = ret
                else:
                    B = 0
                    A[j] = 0
                    C[j-i+H-1] = 0

    # print(DP)

    print(DP[-1][-1])


main()
