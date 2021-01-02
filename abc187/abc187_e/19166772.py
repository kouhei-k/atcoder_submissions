def main():
    import sys
    import collections
    input = sys.stdin.buffer.readline
    N = int(input())
    G = [set() for i in range(N)]
    ab = []
    A = [set() for i in range(N)]
    B = [set() for i in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].add(b)
        G[b].add(a)
        ab.append((a, b))
    Q = int(input())
    C = [0]*N
    s = set([0])
    depth = [0]*N
    q = collections.deque([0])
    s = set([0])
    while(q):
        x = q.popleft()
        for y in G[x]:
            if y in s:
                continue
            else:
                s.add(y)
                q.append(y)
                depth[y] = depth[x] + 1

    for i in range(Q):
        t, e, x = map(int, input().split())
        e -= 1
        a, b = ab[e]
        if depth[a] > depth[b]:
            t ^= 3
            a, b = b, a
        if t == 1:
            C[0] += x
            C[b] -= x
        else:
            C[b] += x

    q.append(0)

    s = set([0])
    while(q):
        x = q.popleft()
        for y in G[x]:
            if y in s:
                continue
            else:
                C[y] += C[x]
                q.append(y)
                s.add(y)

    print(*C, sep='
')


main()
