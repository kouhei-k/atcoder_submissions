import collections
N, M = map(int, input().split())
ab = [tuple(map(int, input().split())) for i in range(M)]

G = [set() for i in range(N)]

for a, b in ab:
    a -= 1
    b -= 1
    G[a].add(b)
    G[b].add(a)

ans = 0
for a, b in ab:
    a -= 1
    b -= 1
    q = collections.deque([0])
    r = [1]*N
    r[0] = 1
    while(q):
        x = q.popleft()
        for y in G[x]:
            if (x == a and y == b) or (x == b and y == a):
                continue
            else:
                if r[y]:
                    r[y] = 0
                    q.append(y)
    if sum(r) > 0:
        ans += 1
print(ans)
