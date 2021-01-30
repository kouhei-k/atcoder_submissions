def main():
    import sys
    input = sys.stdin.buffer.readline
    import bisect

    class segment_tree:
        n = 0
        segtree = []

        def __init__(self, A, func, def_v=0, max_n=2**31 - 1):
            self.N = len(A)

            self.n = (self.N-1).bit_length()
            self.n = 2 ** self.n
            self.func = func
            self.segtree = [def_v]*(2*self.n)
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

    N = int(input())
    a = list(map(int, input().split()))

    A = [0]*N
    ans = 0
    d = dict()

    def func(a, b):
        return(a+b)

    G = segment_tree(A, func)

    for i in range(N):
        G.update(a[i], 1)
        ans += G.query(a[i]+1, N)
    A = sorted(a)
    print(ans)
    for i in range(N-1):
        id = bisect.bisect_left(A, a[i])
        id2 = bisect.bisect_right(A, a[i])

        ans += (N-id2)
        ans -= id

        print(ans)
main()
