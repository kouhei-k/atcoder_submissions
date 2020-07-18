def main():
    # import copy
    import sys
    input = sys.stdin.readline
    R, C, K = map(int, input().split())
    s = [input() for i in range(R)]

    G = [[0]*C for i in range(R)]

    for i in range(R):
        for j in range(C):
            if s[i][j] == 'x':
                G[i][j] = 1
    ans = 0
    sum = 0
    K -= 1

    G = tuple(G)
    D = [0]*(R-2*K)

    # T = [[" "]*C for i in range(R)]

    # prev = []

    for i in range(K, R-K):
        for j in range(K, C-K):
            if i == K and j == K:
                for I in range(K):
                    II = i - K + I
                    for J in range(j-I, j+1+I):
                        sum += G[II][J]
                        # T[II][J] = '■'

                for I in range(K):
                    II = i + K - I
                    for J in range(j-I, j+1+I):
                        sum += G[II][J]
                        # T[II][J] = '■'

                for J in range(j-K, j+K+1):
                    sum += G[i][J]
                #     T[i][J] = '■'
                # prev = copy.deepcopy(T)
                D[i-K] = sum

            elif j == K:
                sum = D[i-K-1]
                # T = copy.deepcopy(prev)

                for k in range(K):
                    sum -= G[i-K+k][j-k-1]
                    sum += G[i+K-k-1][j-k-1]
                    # T[i-K+k][j-k-1] = ' '
                    # T[i+K-k-1][j-k-1] = '■'

                for k in range(K):
                    sum -= G[i-K+k][j+k+1]
                    sum += G[i+K-k-1][j+k+1]
                    # T[i-K+k][j+k+1] = ' '
                    # T[i+K-k-1][j+k+1] = '■'

                sum -= G[i-K-1][j]
                sum += G[i+K][j]

                # T[i-K-1][j] = ' '
                # T[i+K][j] = '■'
                # prev = copy.deepcopy(T)
                D[i-K] = sum
            else:
                for k in range(K):
                    sum += G[i-K+k][j+k]
                    sum -= G[i-K+k][j-k-1]

                    # T[i-K+k][j+k] = '■'
                    # T[i-K+k][j-k-1] = ' '

                sum -= G[i][j-K-1]
                sum += G[i][j+K]

                # T[i][j-K-1] = ' '
                # T[i][j+K] = '■'

                for k in range(K):
                    sum += G[i+K-k][j+k]
                    sum -= G[i+K-k][j-k-1]

                    # T[i+K-k][j+k] = '■'
                    # T[i+K-k][j-k-1] = ' '

            # print(sum, i, j)
            if sum == 0:
                ans += 1
            # T[i][j] = '○'
            # t = ['']*C
            # for I in range(R):
                # for J in range(C):
                #     if G[I][J] == 1:
                #         t[J] = 'x'
                #     else:
                #         t[J] = T[I][J]
                # print("".join(t))
            #     print("".join(T[I]))

            # T[i][j] = '■'
    print(ans)


main()
