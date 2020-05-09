N, K = map(int, input().split())
d = ((N-2)+1)*(N-2)//2
# 一番多いパターンは、1つの頂点に他のすべての頂点が隣接しているパターン

if d < K:
    print(-1)
    exit(0)

ret = N-1 + (d - K)
print(ret)
# 頂点１にすべての頂点をつけていく
for i in range(2, N+1):
    print(1, i)
d -= K
idl = 2
idr = 3
while(d):
    print(idl, idr)
    d -= 1
    idr += 1
    if idr > N:
        idl += 1
        idr = idl+1
