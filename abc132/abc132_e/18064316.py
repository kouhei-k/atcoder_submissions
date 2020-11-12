def main():
    import sys
    import collections
    input = sys.stdin.buffer.readline
    N, M = map(int, input().split())
    G = [set() for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].add(v)
    q = collections.deque()

    S, T = map(int, input().split())
    S -= 1
    T -= 1

    s = set()
    D = [-1]*(3*N)

    for y in G[S]:
        s.add(y*3)
        D[y*3] = 0
        q.append((y*3, 1))

    while(q):
        x, c = q.popleft()
        for y in G[x//3]:
            k = y*3 + c
            if k in s:
                continue
            else:
                D[k] = D[x]
                s.add(k)
                if c + 1 == 3:
                    D[k] += 1
                q.append((k, (c+1) % 3))
    # print(D)
    print(D[3*T + 2])


main()
