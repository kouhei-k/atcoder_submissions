import heapq
import bisect
N = int(input())
a = list(map(int, input().split()))

b = a[:N]
c = a[-N:]
L = [0]*(N+1)
R = [0]*(N+1)

L[0] = sum(b)


heapq.heapify(b)

R[-1] = sum(c)
c = list(map(lambda x: -x, c))
heapq.heapify(c)

for i in range(N):
    k = a[i+N]
    x = heapq.heappop(b)
    if x < k:
        L[i+1] = L[i] + k - x
        heapq.heappush(b, k)
    else:
        L[i+1] = L[i]
        heapq.heappush(b, x)

for i in range(N-1, -1, -1):
    k = a[i+N]
    x = heapq.heappop(c)
    if -x > k:
        heapq.heappush(c, -k)
        R[i] = R[i+1] + x + k
    else:
        R[i] = R[i+1]
        heapq.heappush(c, x)
ans = -10**14
for i in range(N+1):
    ans = max(ans, L[i]-R[i])
#print(L, R)
print(ans)
