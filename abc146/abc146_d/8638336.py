import collections
import sys
input = sys.stdin.readline
N = int(input())
ab = [list(map(int, input().split())) for i in range(N-1)]
eda = [set() for i in range(N)]
for a, b in ab:
    eda[a-1].add(b)
    eda[b-1].add(a)
max_e = 0
for i in range(N-1):
    max_e = max(max_e, len(eda[i]))
id = 0
for i in range(N):
    if len(eda[i]) == max_e:
        id = i

q = collections.deque([(id, 0)])
print(max_e)
d = dict()
for a, b in ab:
    d[(a-1, b-1)] = 0
    d[(b-1, a-1)] = 0
eda2 = [set() for j in range(N)]

g = [set() for i in range(N)]

for a, b in ab:
    g[a-1].add(b-1)
    g[b-1].add(a-1)


while(q):
    x, color = q.popleft()
    i = 1
    for y in g[x]:
        if i == color:
            i += 1
        d[(x, y)] = i
        d[(y, x)] = i
        g[y].remove(x)
        q.append((y, i))
        i += 1

for a, b in ab:
    print(d[(a-1, b-1)])
