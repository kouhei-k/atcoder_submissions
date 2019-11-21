import bisect
import collections
s = input()
t = input()

table = collections.defaultdict(list)
table2 = collections.defaultdict(int)
last = t[-1]
last_id = []
for i, x in enumerate(s):
    table[x].append(i)

for i, x in enumerate(t):
    if x not in table:
        print(-1)
        exit(0)

tmp = 0
id = 0
ans = 0
for x in t:
    l = len(table[x])
    i = bisect.bisect_left(table[x], id)
    if l == i:
        id = 0
        ans += len(s)
        i = bisect.bisect_left(table[x], id)
    id = table[x][i]+1

ans += id


print(ans)
