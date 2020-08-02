import math
from heapq import heappop
import heapq
N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = max(A)+1

while(l+1 < r):
    m = (l+r)//2
    tmp = 0
    for a in A:
        tmp += math.ceil(a / m)-1
    if tmp <= K:
        r = m
    else:
        l = m

print(r)
