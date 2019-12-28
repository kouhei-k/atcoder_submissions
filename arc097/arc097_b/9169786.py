import collections
import sys


class unionFind:
    parent = []

    def __init__(self, N):
        self.parent = [i for i in range(N)]

    def root(self, x):
        if self.parent[x] == x:
            return(x)
        else:
            self.parent[x] = self.root(self.parent[x])
            return(self.parent[x])

    def same(self, x, y):
        x, y = x-1, y-1
        return(self.root(x) == self.root(y))

    def unite(self, x, y):
        x, y = x-1, y-1
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        else:
            self.parent[x] = y
            return


input = sys.stdin.readline
N, M = map(int, input().split())
p = list(map(int, input().split()))
xy = [tuple(map(int, input().split())) for i in range(M)]
ans = 0
t = unionFind(N)

for x, y in xy:
    t.unite(x, y)

for i in range(N):
    if t.same(i+1, p[i]):
        ans += 1
print(ans)
