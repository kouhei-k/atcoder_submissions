def main():
    import sys
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    H, W = map(int, input().split())
    a = [tuple(map(int, input().split())) for i in range(H)]
    g = [[0]*W for i in range(H)]
    mod = 10**9 + 7

    def dfs(i, j):
        ret = g[i][j]
        if ret:
            return(ret)
        else:
            v = a[i][j]
            ret = 1
            if i > 0 and v < a[i-1][j]:
                ret += dfs(i-1, j)
            if i < H-1 and v < a[i+1][j]:
                ret += dfs(i+1, j)
            if j > 0 and v < a[i][j-1]:
                ret += dfs(i, j-1)
            if j < W-1 and v < a[i][j+1]:
                ret += dfs(i, j+1)
            ret %= mod
            g[i][j] = ret
            return(ret)

    ans = 0
    for i in range(H):
        for j in range(W):
            ans += dfs(i, j)
            ans %= mod
    print(ans)
main()
