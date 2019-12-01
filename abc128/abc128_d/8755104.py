import heapq
N, K = map(int, input().split())
V = list(map(int, input().split()))
ans = 0
for k in range(min(K+1, N+1)):
    for i in range(k+1):
        tmp = 0
        tmp2 = []
        heapq.heapify(tmp2)

        for j in range(k-i):
            tmp += V[j]
            if V[j] < 0:
                heapq.heappush(tmp2, V[j])
        for j in range(i):
            tmp += V[N-1-j]
            if V[N-1-j] < 0:

                heapq.heappush(tmp2, V[N-1-j])

        for j in range(min(k, K-k)):
            if len(tmp2) == 0:
                break
            tmp -= heapq.heappop(tmp2)
        ans = max(tmp, ans)


print(ans)
