import heapq
import collections
N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(N)]
table = collections.defaultdict(list)
for a, b in AB:
    table[a].append(b)

job = []
ans = 0
heapq.heapify(job)
for i in range(M):
    for x in table[i+1]:
        heapq.heappush(job, -1 * x)
    if job:
        ans -= heapq.heappop(job)

print(ans)
