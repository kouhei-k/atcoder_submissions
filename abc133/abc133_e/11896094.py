def main():
    import collections
    N, K = map(int, input().split())
    G = [set() for i in range(N)]

    for i in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].add(b)
        G[b].add(a)

    q = collections.deque()
    q.append((0))
    ans = K
    mod = 10**9+7
    r = [True]*N
    r[0] = False
    while(q):
        x = q.popleft()
        tmp = K - 1
        if x > 0:
            tmp -= 1
        for y in G[x]:
            if r[y]:
                r[y] = False
                q.append(y)
                ans *= tmp
                tmp -= 1
                ans %= mod
    print(ans)


main()
