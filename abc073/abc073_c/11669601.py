import sys
import collections
N = int(input())
input = sys.stdin.readline
d = collections.defaultdict(int)
for i in range(N):
    a = int(input())
    d[a] += 1
ans = 0
for x in d:
    if d[x] % 2 == 1:
        ans += 1
print(ans)
