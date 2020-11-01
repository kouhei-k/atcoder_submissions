N = int(input())
xy = [tuple(map(int, input().split())) for i in range(N)]

D = []
D.append((N-1, N, (100 - xy[N-1][1])**2))
D.append((N-1, N+1, ((xy[N-1][1] + 100))**2))
for i in range(N-1):
    D.append((i, N, ((100 - xy[i][1]))**2))
    D.append((i, N+1, ((xy[i][1] + 100))**2))
    for j in range(i+1, N):
        r = (xy[j][0] - xy[i][0])**2 + (xy[j][1]-xy[i][1])**2
        D.append((i, j, r))


D.sort(key=lambda x: x[2], reverse=True)
# print(D)


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


U = unionFind(N+2)
ans = 0
while(U.parent[N] != U.parent[N+1]):
    x, y, ans = D.pop()
    # print(x, y)
    # print(ans)
    U.unite(x+1, y+1)
    U.root(N)
    U.root(N+1)

print((ans**0.5) / 2)
