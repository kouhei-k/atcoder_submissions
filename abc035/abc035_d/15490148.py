import collections
N, M, T = map(int, input().split())
A = list(map(int, input().split()))
G = [set() for i in range(N)]
G2 = [set() for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a].add((b, c))
    G2[b].add((a, c))

q = collections.deque()
q.append((0, 0))

d = [10**10]*N
d[0] = 0

while(q):
    x, c = q.popleft()
    for y, cost in G[x]:
        if d[y] > c + cost:
            d[y] = c + cost
            q.append((y, d[y]))

d2 = [10**10]*N
d2[0] = 0
q.append((0, 0))
while(q):
    x, c = q.popleft()
    for y, cost in G2[x]:
        if d2[y] > c + cost:
            d2[y] = c + cost
            q.append((y, d2[y]))

ans = 0

for i in range(N):
    if A[i] * (T - d[i] - d2[i]) > ans:
        ans = A[i] * (T - d[i] - d2[i])

print(ans)
