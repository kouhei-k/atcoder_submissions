import heapq
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [0]*N
A = 0
B = 0
hq = []
for i in range(N):
    A = max(A, a[i])
    heapq.heappush(hq, -A*b[i])
    c[i] = -hq[0]

print(*c, sep='
')
