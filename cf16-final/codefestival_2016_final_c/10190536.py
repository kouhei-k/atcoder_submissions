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
N,M=map(int,input().split())
G=unionFind(M)
s=set()
for i in range(N):
  tmp=tuple(map(int,input().split()))
  s.add(tmp[1]-1)
  for x in tmp[2:]:
    G.unite(tmp[1],x)

parent=set()
for i in s:
  parent.add(G.root(i))

if len(parent)==1:
  print("YES")
else:
  print("NO")
      
