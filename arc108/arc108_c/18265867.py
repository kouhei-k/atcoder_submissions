def main():
    import sys
    import collections
    input = sys.stdin.buffer.readline
    N, M = map(int, input().split())

    G = [set() for i in range(N)]
    d = dict()
    for i in range(M):
        u, v, c = map(int, input().split())
        u -= 1
        v -= 1
        d[(u, v)] = c
        d[(v, u)] = c
        G[u].add(v)
        G[v].add(u)

    q = collections.deque()
    q.append((0, -1))
    ans = [0]*N

    while(q):
        x, prev = q.popleft()

        for y in G[x]:
            if ans[y] == 0:
                q.append((y, x))
        if prev == -1:
            ans[x] = 1
        else:
            if ans[prev] == d[(x, prev)]:
                ans[x] = d[(x, prev)] % N+1
            else:
                ans[x] = d[(x, prev)]
    print(*ans, sep='
')


main()
