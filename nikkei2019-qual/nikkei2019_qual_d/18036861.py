def main():
    import sys
    import collections

    input = sys.stdin.buffer.readline
    N, M = map(int, input().split())

    G = [set() for i in range(N)]
    G2 = [set() for i in range(N)]
    s = set([i for i in range(N)])
    for i in range(N+M-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].add(b)
        if b in s:
            s.remove(b)
    root = s.pop()
    q = collections.deque([root])
    s = set()
    q2 = collections.deque([root])

    def topological_sort(G, root):
        q = collections.deque([root])
        N = len(G)
        ind = [0]*N
        for i in range(N):
            for y in G[i]:
                ind[y] += 1
        ret = []
        while(q):
            x = q.popleft()
            ret.append(x)
            for y in G[x]:
                ind[y] -= 1
                if ind[y] == 0:
                    q.append(y)
        return(ret)
    q = topological_sort(G, root)
    q = q[::-1]
    parent = [0]*N

    while(q):
        x = q.pop()
        for y in G[x]:
            parent[y] = x + 1

    print(*parent, sep='
')


main()
