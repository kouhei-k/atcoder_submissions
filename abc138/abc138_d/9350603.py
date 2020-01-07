

import collections
N, Q = map(int, input().split())
g = [set() for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].add(b)
    g[b].add(a)

parent = [-1 for i in range(N)]
parent[0] = 0

q = collections.deque()
q.append(0)

point = [0 for i in range(N)]

for i in range(Q):
    p, x = map(int, input().split())
    p -= 1
    point[p] += x

while(q):
    x = q.popleft()
    for y in g[x]:
        if parent[y] == -1:
            q.append(y)
            parent[y] = x
            point[y] += point[x]

print(" ".join(map(str, point)))
