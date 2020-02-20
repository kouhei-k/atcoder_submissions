import itertools
import collections
N = int(input())
A = list(map(int, input().split()))

table = collections.defaultdict(int)
A = [0] + A
s = itertools.accumulate(A)
for x in s:
    table[x] += 1
ans = 0
for x in table:
    if table[x] > 1:
        ans += (table[x] * (table[x]-1)) // 2
print(ans)
