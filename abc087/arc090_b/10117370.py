N, M = map(int, input().split())
LRD = [tuple(map(int, input().split())) for i in range(M)]


class unionFind:
    parent = []

    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.weight = [0]*N

    def root(self, x):
        if self.parent[x] == x:
            return(x)
        else:
            p = self.root(self.parent[x])
            self.weight[x] += self.weight[self.parent[x]]
            self.parent[x] = p
            return(self.parent[x])

    def same(self, x, y):
        x, y = x-1, y-1
        return(self.root(x) == self.root(y))

    def unite(self, x, y, w):
        w -= self.getWeight(x)
        w += self.getWeight(y)
        x, y = x-1, y-1
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        else:
            self.parent[x] = y
            self.weight[x] = self.weight[y]+w
            return

    def getWeight(self, x):
        x -= 1
        self.root(x)
        return(self.weight[x])


G = unionFind(N)
flag = True

for l, r, d in LRD:
    if G.same(l, r) == False:
        G.unite(l, r, d)
    else:
        if G.getWeight(l) - G.getWeight(r) == d:
            continue
        else:
            flag = False
            break

if flag:
    print("Yes")
else:
    print("No")
