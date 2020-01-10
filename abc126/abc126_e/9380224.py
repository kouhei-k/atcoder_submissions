N,M=map(int,input().split())
xyz=[tuple(map(int,input().split())) for i in range(M)]
class unionFind:
    parent = []
    num=0
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.num=N
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
            self.num-=1
            return
G=unionFind(N)
for x,y,z in xyz:
  G.unite(x,y)
print(G.num)
