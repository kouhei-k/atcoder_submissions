import sys
sys.setrecursionlimit(10**5)


class unionFind:
    parent = []
    nums = []

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.nums = [1]*n

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
            self.nums[y] += self.nums[x]
            self.nums[x] = 0
            return


N, M = map(int, input().split())
G = unionFind(N)
ans = [0]*M
ab = [tuple(map(int, input().split())) for i in range(M)]

tmp = (N * (N-1)) // 2
for i, x in enumerate(reversed(ab)):
    a, b = x[0], x[1]
    ans[M-1-i] = tmp
    a = G.root(a-1)
    b = G.root(b-1)
    if a == b:
        continue
    else:
        tmp -= G.nums[a] * G.nums[b]
        G.parent[a] = b
        G.nums[b] += G.nums[a]
        G.nums[a] = 0


for i in range(M):
    print(ans[i])
