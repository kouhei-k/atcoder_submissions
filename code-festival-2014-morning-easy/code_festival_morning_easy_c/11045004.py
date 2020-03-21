def main():
    from scipy.sparse.csgraph import dijkstra, csgraph_from_dense
    n, m = map(int, input().split())
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    g = [[-1]*n for i in range(n)]
    for i in range(m):
        x, y, d = map(int, input().split())
        x -= 1
        y -= 1
        g[x][y] = d
        g[y][x] = d

    G = csgraph_from_dense(g, null_value=-1)

    sd = dijkstra(G, indices=s)
    td = dijkstra(G, indices=t)
    ans = -1

    for i, xy in enumerate(zip(sd, td)):
        x, y = xy
        if x == y and x <= 1000:
            ans = i+1
            break
    print(ans)


main()
