import collections
import heapq
N, M = map(int, input().split())
a = list(map(int, input().split()))


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


G = unionFind(N)
for i in range(M):
    x, y = map(int, input().split())
    G.unite(x+1, y+1)
A = [(a[i], i) for i in range(N)]


A.sort(key=lambda x: (-G.getCount(x[1]), G.parent[x[1]], x[0]))
a1 = 0
x = 0
ans = 0
t = []
for a, x in A:
    x = G.root(x)
    if len(t) > 0:
        if G.root(t[0][1]) == x:
            heapq.heappush(t, (a, x))
        else:
            a1, y = heapq.heappop(t)
            y = G.root(y)
            ans += (a + a1)
            G.unite(x+1, y+1)
    else:
        heapq.heappush(t, (a, x))

s = set()
for i in range(N):
    s.add(G.root(i))
if len(s) == 1:
    print(ans)
else:
    print("Impossible")
    # print(ans)
    # print(s)
