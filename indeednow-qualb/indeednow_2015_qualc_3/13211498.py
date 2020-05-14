import heapq
N = int(input())
G = [set() for i in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].add(b)
    G[b].add(a)

hq = []
r = [0]*N

hq = [0]
arr = []
while(hq):
    x = heapq.heappop(hq)
    arr.append(x+1)
    r[x] = 1
    for y in G[x]:
        if r[y]:
            continue
        heapq.heappush(hq, y)
        r[y] = 1

print(*arr)
