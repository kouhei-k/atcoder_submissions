import collections
N, Q = map(int, input().split())
G = [set() for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].add(b)
    G[b].add(a)

d = collections.defaultdict(int)

for i in range(Q):
    p, x = map(int, input().split())
    p -= 1
    d[p] += x

q = collections.deque()

r = [-1]*N
r[0] = d[0]
q.append(0)
while(q):
    x = q.popleft()
    c = r[x]
    for y in G[x]:
        if r[y] < 0:
            r[y] = c+d[y]
            q.append(y)

print(*r)
