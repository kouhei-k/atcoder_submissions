import math
import bisect


n = int(input())

a = list(map(int, input().split()))
a.sort()

ncr = 0
ans = [0, 0]

id = bisect.bisect_left(a[:n-1], a[n-1]//2)
if abs(a[-1]/2 - a[id]) < abs(a[-1]/2 - a[id-1]):
    ans = id
else:
    ans = id-1

print(a[-1], a[ans])
