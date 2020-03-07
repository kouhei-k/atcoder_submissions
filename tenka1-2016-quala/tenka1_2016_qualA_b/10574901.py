import collections
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
G = [set() for i in range(N)]

for i in range(1, N):
    p = int(input())
    G[p].add(i)
d = collections.defaultdict(int)
for i in range(M):
    b, c = map(int, input().split())
    d[b] = c

m = [10**9]*N
m[0] = 0


def solve(i):

    if i in d:
        m[i] = d[i]
        return(m[i])
    else:
        for x in G[i]:
            m[i] = min(m[i], solve(x))
        return(m[i])


q = collections.deque()
q.append((0))  # 番号とそこまでの　PackDropの個数
ans = 0
solve(0)
while(q):
    x = q.popleft()

    for z in G[x]:
        ans += m[z] - m[x]
        q.append(z)

print(ans)
