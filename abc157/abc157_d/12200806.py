import collections
import sys
sys.setrecursionlimit(10**5)
N, M, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(M)]

CD = [tuple(map(int, input().split())) for i in range(K)]


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


# F = [set() for i in range(N)]
F = unionFind(N)
f = [set() for i in range(N)]
for a, b in AB:
    F.unite(a, b)
    a -= 1
    b -= 1
    f[a].add(b)
    f[b].add(a)

B = [set() for i in range(N)]
for c, d in CD:
    c -= 1
    d -= 1
    B[c].add(d)
    B[d].add(c)

ans = [0]*N
D = collections.defaultdict(set)
for i in range(N):
    D[F.root(i)].add(i)

# print(f)
for i in range(N):
    x = D[F.root(i)]
    ret = len(x)
    ret -= 1
    ret -= len(x & f[i])
    ret -= len(x & B[i])
    ans[i] = ret
print(*ans)
