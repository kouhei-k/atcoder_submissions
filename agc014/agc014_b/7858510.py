import collections
N, M = map(int, input().split())
a = [0]*M
b = [0]*M
for i in range(M):
    a[i], b[i] = map(int, input().split())
table = collections.defaultdict(int)

for i in range(M):
    table[a[i]] += 1
    table[b[i]] += 1

odd = []
for x in table:
    if table[x] % 2 == 1:
        odd.append(x)

if len(odd) > 0:
    print("NO")
else:
    print("YES")
