def main():
    import networkx as nx
    import sys
    input = sys.stdin.buffer.readline
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for i in range(N-1+M)]
    DG = nx.DiGraph(AB)

    G = [set() for i in range(N)]
    for a, b in AB:
        a -= 1
        b -= 1
        G[a].add(b)

    DG = list(nx.topological_sort(DG))

    parent = [0]*N
    for i, x in enumerate(DG):
        x -= 1
        if i == 0:
            parent[x] = 0
        for y in G[x]:
            parent[y] = x+1
    print(*parent, sep='
')


main()
