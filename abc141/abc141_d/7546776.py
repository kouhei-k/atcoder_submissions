import heapq
N, M = map(int, input().split())

A = list(map(int, input().split()))

hq = []

for i in range(N):
    heapq.heappush(hq, -(A[i]))


while(M):
    k = heapq.heappop(hq) * -1
    k = k // 2
    heapq.heappush(hq, -k)
    M -= 1
ans = 0
for i in range(N):
    ans += heapq.heappop(hq)

print(-ans)
