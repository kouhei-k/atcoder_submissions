def main():
    import sys
    input = sys.stdin.buffer.readline
    R, C, K = map(int, input().split())
    d = dict()
    for i in range(K):
        r, c, v = map(int, input().split())
        r -= 1
        c -= 1
        d[(r, c)] = v

    # DP = [[[0, -1, -1, -1] for i in range(C)] for j in range(R+1)]
    prev = [0 for i in range(C)]
    DP = [[0, -1, -1, -1] for i in range(C)]
    for i in range(R):
        DP[0][0] = prev[0]
        if (i, 0) in d:
            DP[0][1] = d[(i, 0)] + prev[0]

        prev[0] = max(DP[0])

        for j in range(1, C):
            if (i, j) in d:
                for k in range(3):
                    if DP[j-1][k] == -1:
                        break
                    else:
                        DP[j][k+1] = max(DP[j-1][k+1], DP[j-1]
                                         [k] + d[(i, j)], prev[j] + d[(i, j)])
            else:
                for k in range(1, 4):
                    DP[j][k] = DP[j-1][k]

            DP[j][0] = max(DP[j-1][0], prev[j])

            prev[j] = max(DP[j])
        # print(prev)
    print(prev[-1])


main()
