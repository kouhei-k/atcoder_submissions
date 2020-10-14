import sys
sys.setrecursionlimit(2*10**5)


class unionFind:
    parent = []
    counter = []

    def __init__(self, N, A):
        self.parent = [i for i in range(N)]
        self.counter = [1]*N

    def root(self, x):
        if self.parent[x] == x:
            return(x)
        else:
            self.parent[x] = self.root(self.parent[x])
            return(self.parent[x])

    def count(self, x):
        if self.parent[x] == x:
            return(self.counter[x])
        else:
            self.parent[x] = self.root(self.parent[x])
            self.counter[x] = self.counter[self.parent[x]]
            return(self.counter[x])

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
            self.counter[y] += self.counter[x]
            self.counter[x] = self.counter[y]
            return


def main():
    import heapq

    input = sys.stdin.buffer.readline
    N = int(input())
    xy = [tuple(list(map(int, input().split()))) for i in range(N)]
    Y = [None]*N
    for i in range(N):
        x, y = xy[i]
        Y[x-1] = (y, i)

    # print(xy)
    U = unionFind(N, xy)
    hq = []
    s = []
    for y, i in Y:
        r = N
        id = N
        flag = False
        while(s):
            y2, j = heapq.heappop(s)
            if y2 < y:
                U.unite(i+1, j+1)
                if flag == False:
                    flag = True
                    r = y2
                    id = j
            else:
                heapq.heappush(s, (y2, j))
                break

        if flag:
            heapq.heappush(s, (r, id))
        else:
            heapq.heappush(s, (y, i))

    for i in range(N):
        U.count(i)
        print(U.counter[i])


main()
