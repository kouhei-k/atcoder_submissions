def main():
    import sys
    input = sys.stdin.buffer.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    class segment_tree:
        n = 0
        segtree = []
        max_v = 10**10

        def __init__(self, A, max_n=2**31 - 1):
            self.N = len(A)
            self.max_v = max_n
            self.n = (self.N-1).bit_length()
            self.n = 2 ** self.n
            self.segtree = [0]*(2*self.n)
            for i in range(self.N):
                self.segtree[self.n+i - 1] = A[i]
            for i in range(self.n - 2, -1, -1):
                self.segtree[i] = self.segtree[i*2 + 1] ^ self.segtree[i*2 + 2]

        def update(self, i, x):
            id = self.n+i - 1
            self.segtree[id] = x
            while(id > 0):
                id = (id - 1) // 2
                self.segtree[id] = self.segtree[id *
                                                2 + 1] ^ self.segtree[id*2+2]
                #print(self.segtree[id*2 + 1], self.segtree[id*2+2])

    # queryはまだ

        def query(self, a, b, k, l, r):
            # a < bじゃないとmax_vが返ってしまうので、 A_a から A_bまでをやりたいときはb+1を使う
            if r <= a or l >= b:
                return(0)
            if a <= l and r <= b:
                return(self.segtree[k])
            else:
                vl = self.query(a, b, k*2+1, l, (l+r)//2)
                vr = self.query(a, b, k*2+2, (l+r)//2, r)
                return(vl ^ vr)

    G = segment_tree(A)

    for i in range(Q):
        t, x, y = map(int, input().split())
        x -= 1
        if t == 1:
            G.update(x, A[x] ^ y)
            A[x] ^= y
        else:
            print(G.query(x, y, 0, 0, G.n))


main()
