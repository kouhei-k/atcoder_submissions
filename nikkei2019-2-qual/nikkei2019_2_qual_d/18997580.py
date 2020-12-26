def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    D = [set() for i in range(N)]
    for i in range(M):
        L, R, C = map(int, input().split())
        L -= 1
        R -= 1
        D[R].add((L, C))

    dp = [10**15]*N
    dp[0] = 0

    class segment_tree:
        n = 0
        segtree = []

        def __init__(self, A, func, default_v=2**31 - 1):
            self.N = len(A)
            self.default = default_v
            self.n = (self.N-1).bit_length()
            self.n = 2 ** self.n
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
            ret = self.default
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

    G = segment_tree(dp, min, 10**15)
    for i in range(N):
        for L, C in D[i]:
            k = G.query(L, i)
            if dp[i] > k+C:
                dp[i] = k+C
                G.update(i, k+C)
    if dp[-1] < 10**15:
        print(dp[-1])
    else:
        print(-1)


main()
