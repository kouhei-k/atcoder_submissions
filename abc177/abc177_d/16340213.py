import collections
import sys
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(M)]


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


G = unionFind(N)

for a, b in AB:
    G.unite(a, b)

for i in range(N):
    G.root(i)

C = collections.Counter(G.parent).most_common()

print(C[0][1])
