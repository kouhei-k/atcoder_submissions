import collections
N, K = map(int, input().split())
a = [list(map(int, input().split())) for i in range(N)]
mod = 998244353

h = set()
v = set()


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


H = unionFind(N)

for i in range(N-1):
    for j in range(i+1, N):
        flag = True
        for k in range(N):
            if a[i][k] + a[j][k] > K:
                flag = False
        if flag:
            H.unite(i+1, j+1)


V = unionFind(N)
for i in range(N-1):
    for j in range(i+1, N):
        flag = True
        for k in range(N):

            if a[k][i] + a[k][j] > K:
                flag = False
        if flag:
            V.unite(i+1, j+1)

p = [0]*N

p[0] = 1
for i in range(1, N):
    p[i] = p[i-1]*(i+1) % mod

for i in range(N):
    H.root(i)
    V.root(i)


CH = collections.Counter(H.parent)
CV = collections.Counter(V.parent)

ans = 1
# print(CH)

for x in CH:
    ans *= p[CH[x]-1]
    ans %= mod
for x in CV:
    ans *= p[CV[x]-1]
    ans %= mod
print(ans)
