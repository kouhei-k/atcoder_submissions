def main():
    m = int(input())
    n = int(input())

    A = [list(map(int, input().split())) for i in range(n)]


    def dfs(i, j, G):
        ret = 0
        if i+1 < n and G[i+1][j]:
            G[i+1][j] = 0
            ret = max(ret, 1+(dfs(i+1, j, G)))

            G[i+1][j] = 1
        if i - 1 >= 0 and G[i-1][j]:
            G[i-1][j] = 0
            ret = max(ret, 1 + (dfs(i-1, j, G)))
            G[i-1][j] = 1

        if j+1 < m and G[i][j+1]:
            G[i][j+1] = 0
            ret = max(ret, 1+(dfs(i, j+1, G)))

            G[i][j+1] = 1

        if j - 1 >= 0 and G[i][j-1]:
            G[i][j-1] = 0
            ret = max(ret, 1 + (dfs(i, j-1, G)))
            G[i][j-1] = 1
        return(ret)


    ans = 0
    for i in range(n):
        for j in range(m):
            if A[i][j]:
                ans = max(ans, dfs(i, j, A))
    print(ans)
main()
