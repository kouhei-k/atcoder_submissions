import collections
N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
G = [set() for i in range(N)]
for i in range(M):
    c, d = map(int, input().split())
    c -= 1
    d -= 1

    G[c].add(d)
    G[d].add(c)
flag = False
if sum(a) == sum(b):
    flag = True
s = set()
q = collections.deque()
for i in range(N):
    if i not in s:
        q.append(i)
        s.add(i)
    else:
        continue
    A = 0
    B = 0
    while(q):
        x = q.popleft()
        A += a[x]
        B += b[x]
        for y in G[x]:
            if y in s:
                continue
            else:
                s.add(y)
                q.append(y)

    if A != B:
        print("No")
        exit(0)

print("Yes")
