import collections
N = int(input())
G = [set() for i in range(N)]
ab = [tuple(map(int, input().split())) for i in range(N-1)]

d = dict()
i = 0
for a, b in ab:
    a -= 1
    b -= 1
    d[(a, b)] = i
    d[(b, a)] = i
    i += 1
    G[a].add(b)
    G[b].add(a)


q = collections.deque()
r = set()
r.add(0)
q.append((0, 0))
ans = [0]*(N-1)

while(q):
    x, s = q.popleft()
    i = 1
    for y in G[x]:
        if y in r:
            continue
        else:
            r.add(y)
            if i == s:
                i += 1
            ans[d[(x, y)]] = i
            q.append((y, i))
            i += 1
print(max(ans))
print(*ans, sep='
')
