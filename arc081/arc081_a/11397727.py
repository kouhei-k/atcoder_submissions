import heapq
import collections
N = int(input())
A = list(map(int, input().split()))

table = collections.defaultdict(int)
hq = [0, 0]
for x in A:
    table[x] += 1
    if table[x] == 2:
        heapq.heappush(hq, -x)
        table[x] = 0
print(heapq.heappop(hq) * heapq.heappop(hq))
