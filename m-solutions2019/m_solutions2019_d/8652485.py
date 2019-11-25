import heapq
import sys
sys.setrecursionlimit(20000)
N = int(input())
ab = [tuple(map(int, input().split())) for i in range(N-1)]
c = list(map(int, input().split()))

print(sum(c) - max(c))
c = list(map(lambda x: x*(-1), c))
heapq.heapify(c)
d = [[0, i] for i in range(N)]
g = [set() for i in range(N)]
for a, b in ab:
    d[a-1][0] += 1
    d[b-1][0] += 1
    g[a-1].add(b-1)
    g[b-1].add(a-1)
d.sort(reverse=True, key=lambda x: x[0])
for i in range(N):
    d[i][0] = -1


ans = ["-1"]*N
ans[d[0][1]] = str(-1 * heapq.heappop(c))


def dfs(start):
    for x in g[start]:
        if ans[x] == "-1":
            ans[x] = str(-1 * heapq.heappop(c))
            dfs(x)


dfs(d[0][1])
d.sort(key=lambda x: x[1])


print(" ".join(ans))
