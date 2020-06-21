import collections
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
BC = [tuple(map(int, input().split())) for i in range(Q)]

d = collections.defaultdict(int)

S = sum(A)

for x in A:
    d[x] += 1

for B, C in BC:
    diff = C - B
    S += d[B]*diff
    d[C] += d[B]
    d[B] = 0
    print(S)
