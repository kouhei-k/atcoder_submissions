def main():
    import sys
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    H, W = map(int, input().split())
    a = [tuple(map(int, input().split())) for i in range(H)]
    g = [[0]*W for i in range(H)]
    mod = 10**9 + 7

    def dfs(i, j):
        if g[i][j] > 0:
            return(g[i][j])
        else:
            val = a[i][j]
            ret = 1
            for u, v in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if H > u >= 0 and W > v >= 0 and val < a[u][v]:
                    ret += dfs(u, v)
            ret %= mod
            g[i][j] = ret
            return(ret)

    ans = 0
    for i in range(H):
        for j in range(W):
            ans += dfs(i, j)
            ans %= mod
    # print(g)
    print(ans)


main()
