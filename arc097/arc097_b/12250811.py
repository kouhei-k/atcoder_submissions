N, M = map(int, input().split())
p = list(map(int, input().split()))


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

for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    G.unite(x, y)

ans = 0
for i in range(N):
    if G.same(p[i]-1, i):
        ans += 1

print(ans)
