import heapq
N = int(input())


# その棚の商品がなくなったらそこを選んでほしくない
# ->全部の棚の最後に消費期限0の商品を突っ込む
T = [list(map(int, input().split()))[1:]+[0, 0] for i in range(N)]
M = int(input())
a = list(map(int, input().split()))

A = [[T[i][0], T[i][1]] for i in range(N)]
hq = [[] for i in range(2)]
idx = [2]*N

for i, t in enumerate(A):
    heapq.heappush(hq[0], (-t[0], i))
    heapq.heappush(hq[1], (-t[0], i))
    heapq.heappush(hq[1], (-t[1], i))

r = set()
for i, x in enumerate(a):
    # print(r)
    while(-hq[x-1][0][0] in r):
        t, id = heapq.heappop(hq[x-1])
    t, id = heapq.heappop(hq[x-1])
    t = -t
    print(t)
    if x == 1:
        A[id][0] = A[id][1]
        heapq.heappush(hq[0], (-A[id][0], id))
    else:
        if A[id][0] == t:
            A[id][0] = A[id][1]
            heapq.heappush(hq[0], (-A[id][0], id))

    A[id][1] = T[id][idx[id]]
    heapq.heappush(hq[1], (-A[id][1], id))
    r.add(t)
    idx[id] += 1
