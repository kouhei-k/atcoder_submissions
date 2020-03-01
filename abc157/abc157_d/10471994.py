
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


class unionFind:
    parent = []
    count = []

    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.count = [1 for i in range(N)]

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
            self.count[y] += self.count[x]
            self.count[x] = self.count[y]
            return

    def getCount(self, x):
        self.count[x] = self.count[self.root(x)]
        return(self.count[x])


N, M, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(M)]

CD = [tuple(map(int, input().split())) for i in range(K)]

G = unionFind(N)
for a, b in AB:
    G.unite(a, b)

for i in range(N):
    G.root(i)

ans = [G.getCount(i) - 1 for i in range(N)]
# print(ans)
# print(G.count)
for a, b in AB:
    ans[a-1] -= 1
    ans[b-1] -= 1

for c, d in CD:
    if G.same(c, d):
        ans[c-1] -= 1
        ans[d-1] -= 1

print(*ans)
