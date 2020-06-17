import heapq
N = int(input())
H = list(map(int, input().split()))
ans = [0]*N
hq = []
for i in range(N):
    # print(hq)
    ans[i] = len(hq)
    while(hq and hq[0] < H[i]):
        heapq.heappop(hq)
    heapq.heappush(hq, H[i])

print(*ans, sep='
')
