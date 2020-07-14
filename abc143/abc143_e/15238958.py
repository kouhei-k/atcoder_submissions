from scipy.sparse.csgraph import csgraph_from_dense, shortest_path


def main():
    import heapq
    import sys
    input = sys.stdin.buffer.readline
    N, M, L = map(int, input().split())

    G = [[-1]*N for i in range(N)]

    for i in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        G[A][B] = C
        G[B][A] = C
    g = csgraph_from_dense(G, null_value=-1)
    D = shortest_path(g)
    G2 = [[-1]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if D[i][j] >= 0 and D[i][j] <= L:
                G2[i][j] = 1

    g2 = csgraph_from_dense(G2, null_value=-1)
    D = shortest_path(g2)

    Q = int(input())
    for _ in range(Q):
        s, t = map(int, input().split())
        s -= 1
        t -= 1
        if D[s][t] <= N**2:
            print(int(D[s][t])-1)
        else:
            print(-1)


main()
