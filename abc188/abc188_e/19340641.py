def main():
    import sys
    import collections
    input = sys.stdin.buffer.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    AI = [(A[i], i) for i in range(N)]
    AI.sort()
    G = [set() for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].add(b)
    s = set()
    ans = -10**10
    q = collections.deque()
    for _, i in AI:
        if i in s:
            continue
        q.append((i, 10**10))
        s.add(i)

        while(q):
            x, c = q.popleft()
            if ans < A[x]-c:
                ans = A[x]-c
            if A[x] < c:
                c = A[x]
            for y in G[x]:
                if y in s:
                    if ans < A[y]-c:
                        ans = A[y] - c
                else:
                    q.append((y, c))
                    s.add(y)
    print(ans)


main()
