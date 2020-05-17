import collections
N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(M)]

ans = [0]*N
G = [set() for i in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    G[a].add(b)
    G[b].add(a)

q = collections.deque([0])

r = set()
r.add(0)
while(q):
    x = q.popleft()
    for y in G[x]:
        if y in r:
            continue
        else:
            ans[y] = x+1
            r.add(y)
            q.append(y)

if len(r) < N:
    print('No')
else:
    print("Yes")
    print(*ans[1:], sep='
')
