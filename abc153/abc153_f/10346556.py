import math
import collections
N, D, A = map(int, input().split())
XH = [tuple(map(int, input().split())) for i in range(N)]
XH.sort()
q = collections.deque()
c = 0
ans = 0
for x, h in XH:
    while(q):
        if q[0][0] < x:
            t = q.popleft()
            c -= t[1]
        else:
            break
    h -= c*A
    k = math.ceil(max(h, 0) / A)
    ans += k
    c += k
    if k > 0:
        q.append((x+(2*D), k))
print(ans)
