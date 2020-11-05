def main():
    import sys
    input = sys.stdin.buffer.readline
    N, K = map(int, input().split())

    # sys.setrecursionlimit(10**5)

    class segment_tree:
        n = 0
        segtree = []

        def __init__(self, N, n, A, func, max_n=2**31 - 1):
            self.N = N
            self.n = n
            self.func = func
            self.segtree = [0]*(2*self.n)
            for i in range(self.N):
                self.segtree[self.n+i] = A[i]
            for i in range(self.n - 1, -1, -1):
                self.segtree[i] = self.func(
                    self.segtree[i*2 + 1], self.segtree[i*2])

        def update(self, i, x):
            id = self.n+i
            self.segtree[id] = x
            while(id > 1):
                id = id >> 1
                self.segtree[id] = self.func(
                    self.segtree[id*2], self.segtree[id*2+1])
                #print(self.segtree[id*2 + 1], self.segtree[id*2+2])

        def query(self, a, b):
            l = self.n + a
            r = self.n + b
            ret = 0
            while(l < r):
                if l & 1:
                    ret = self.func(ret, self.segtree[l])
                    l += 1
                if r & 1:
                    r -= 1
                    ret = self.func(ret, self.segtree[r])
                l = l >> 1
                r = r >> 1
            return(ret)

    X = 3*10**5+10
    n = (X-1).bit_length()
    n = 2 ** n
    A = [0]*(3*10**5+10)
    G = segment_tree(N, n, A, max)
    ans = 0
    for _ in range(N):
        a = int(input())
        l = max(a-K, 0)
        r = min(a+K, 3*10**5+10)
        tmp = G.query(l, r+1) + 1
        # print(G.segtree[n:n+N])
        if tmp > ans:
            ans = tmp
        G.update(a, tmp)

    print(ans)


main()
