import bisect
d = int(input())
n = int(input())
m = int(input())

D = [0]*(n+1)
for i in range(n-1):
    D[i+1] = int(input())

D[-1] = d
D.sort()
ans = 0
for i in range(m):
    k = int(input())
    id = bisect.bisect_left(D, k)
    if id > 0:
        ans += min(D[id] - k, k - D[id-1])
    else:
        ans += D[id] - k
print(ans)
