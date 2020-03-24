def main():
    import collections
    H, W = map(int, input().split())
    C = [list(map(int, input().split())) for i in range(H)]

    G = [[0]*(W+1) for i in range(H+1)]
    ans = 0
    for i in range(H):
        tmp = 0
        for j in range(W):
            x = C[i][j]
            if i % 2 != j % 2:
                x = -x
            if i == 0:
                G[i+1][j+1] = G[i+1][j] + x
            else:
                tmp += x
                G[i+1][j+1] = G[i][j+1] + tmp

    for l in range(W+1):
        for r in range(l+1, W+1):
            table = collections.defaultdict(int)
            for i in range(H+1):
                v = G[i][r] - G[i][l]
                if i > 0 and v == 0:
                    ans = max(ans, r-l)
                if v in table:
                    ans = max(ans, (i - table[v])*(r-l))
                else:
                    table[v] = i

    print(ans)
    #print(*G, sep="
")


main()
