import sys
sys.setrecursionlimit(10**5)
N=int(input())
xy=[tuple(map(int,input().split())) for i in range(N)]
xy = [(i, xy[i][0], xy[i][1]) for i in range(N)]
xy2 = sorted(xy, key=lambda x:x[1])
xy.sort(key=lambda x:x[2])

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

D = []
for i in range(N-1):
  d = xy[i+1][2] - xy[i][2]
  D.append((d,xy[i][0],xy[i+1][0]))
  d = xy2[i+1][1] - xy2[i][1]
  D.append((d,xy2[i][0],xy2[i+1][0]))
U = unionFind(N)
D.sort()
ans = 0
for i in range(2*N - 2):
  d, x, y = D[i]
  if U.same(x,y):
    continue
  else:
    U.unite(x,y)
    ans += d
print(ans)
