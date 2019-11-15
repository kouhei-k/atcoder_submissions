import bisect
N = int(input())
enable = set()

k = 0
while(6**k <= N):
    enable.add(6**k)
    k += 1
k = 0
while(9**k <= N):
    enable.add(9**k)
    k += 1


enable = list(enable)
enable.sort()

ans = 10**9
l = len(enable)
for i in range(l):
    n = N
    tmp = 0
    while(n != 0):
        id = bisect.bisect_right(enable, n) - 1
        if id != 0 and n % enable[id] > 2 and n % enable[id] < 6:
            id -= 1
        n -= enable[id]
        tmp += 1
    enable.pop()

    ans = min(tmp, ans)

print(ans)
