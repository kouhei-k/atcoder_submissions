
class unionFind:
    parent = []
    counter = []

    def __init__(self, N, CL):
        self.parent = [i for i in range(N)]
        self.counter = [1 for i in range(N)]
        self.CL = [dict() for i in range(N)]
        for i, x in enumerate(CL):
            self.CL[i][x] = 1

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
            if self.counter[x] > self.counter[y]:
                x, y = y, x
            self.parent[x] = y
            for z in self.CL[x]:
                if z in self.CL[y]:
                    self.CL[y][z] += self.CL[x][z]
                else:
                    self.CL[y][z] = self.CL[x][z]
                    self.counter[y] += 1
            return


def main():
    import sys
    input = sys.stdin.buffer.readline
    N, Q = map(int, input().split())
    C = list(map(int, input().split()))

    U = unionFind(N, C)

    # q = [map(int, input().split()) for i in range(Q)]

    for _ in range(Q):
        id, a, b = map(int, input().split())

        if id == 1:
            U.unite(a, b)

        elif id == 2:
            a -= 1
            x = U.root(a)
            if b in U.CL[x]:
                print(U.CL[x][b])
            else:
                print(0)
        # print(U.CL)


main()
