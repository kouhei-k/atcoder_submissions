import collections
N = int(input())
d = [0]*N
route = [set() for i in range(N)]
for i in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    route[u].add((v, w))
    route[v].add((u, w))
    d[u] += 1
    d[v] += 1
d = d.index(max(d))
q = collections.deque()
q.append((d, 0))

G = [0]*N

while(q):
    x, l = q.popleft()
    for v, w in route[x]:
        G[v] = w + l
        q.append((v, w+l))
        route[v].remove((x, w))
ans = [0]*N

for i in range(N):
    if i == d:
        continue
    if G[i] % 2 == 1:
        ans[i] = 1
for i in range(N):
    print(ans[i])
