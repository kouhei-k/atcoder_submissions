import math
import collections
N, M = map(int, input().split())
name = input()
kit = input()
table = collections.defaultdict(int)
table2 = collections.defaultdict(int)
for x in kit:
    table[x] += 1
for x in name:
    table2[x] += 1
ans = -1
for x in table2:
    if table[x] == 0:
        ans = -1
        break
    ans = max(math.ceil(table2[x] / table[x]), ans)


print(ans)
