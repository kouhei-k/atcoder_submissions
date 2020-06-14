import sys
import heapq
import collections


class segment_tree:
    n = 0
    segtree = []
    max_v = 10**9

    def __init__(self, A, max_n=10**9 + 1):
        N = len(A)
        self.max_v = max_n
        self.n = (N-1).bit_length()
        self.n = 2 ** self.n
        self.segtree = [max_n]*(2*self.n)
        for i in range(N):
            self.segtree[self.n+i - 1] = A[i]
        for i in range(self.n - 2, -1, -1):
            self.segtree[i] = min(self.segtree[i*2 + 1], self.segtree[i*2 + 2])

    def update(self, i, x):
        id = self.n+i - 1
        self.segtree[id] = x
        while(id):
            id = (id - 1) // 2
            self.segtree[id] = min(
                self.segtree[id*2 + 1], self.segtree[id*2+2])
            # print(self.segtree[id*2 + 1], self.segtree[id*2+2])


input = sys.stdin.buffer.readline
N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]
Y = [[] for i in range(2*10**5+1)]
for i, ab in enumerate(AB):
    A, B = ab
    AB[i][1] = B-1
    heapq.heappush(Y[B-1], (-A, i))
CD = [tuple(map(int, input().split())) for i in range(Q)]
M = 10**9
PP = [0]*(2*10**5+1)

for i, x in enumerate(Y):
    if len(x) > 0:
        PP[i] = -x[0][0]
    else:
        PP[i] = 10**9+1

G = segment_tree(PP)

for C, D in CD:
    C -= 1
    D -= 1
    p = AB[C][1]

    heapq.heappush(Y[D], (-AB[C][0], C))
    AB[C][1] = D

    while(Y[p]):
        # print(*AB)
        # print(AB[Y[p][0][1]], p)
        if AB[Y[p][0][1]][1] == p:
            break
        else:
            heapq.heappop(Y[p])

    if len(Y[D]) > 0:
        G.update(D, -Y[D][0][0])
    else:
        G.update(D, 10**9)

    if len(Y[p]) > 0:
        G.update(p, -Y[p][0][0])
    else:
        G.update(p, 10**9)

    print(G.segtree[0])
