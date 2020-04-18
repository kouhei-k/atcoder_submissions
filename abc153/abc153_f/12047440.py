import math
import collections
N, D, A = map(int, input().split())

XH = [tuple(map(int, input().split())) for i in range(N)]
XH.sort()
q = collections.deque()
c = 0
ans = 0
for x, h in XH:
    while(q and q[0][0] < x):
        c -= q[0][1]
        q.popleft()
    h -= c * A
    if h < 0:
        h = 0
    ans += math.ceil(h/A)
    c += math.ceil(h/A)

    q.append((x+2*D, math.ceil(h/A)))

print(ans)
