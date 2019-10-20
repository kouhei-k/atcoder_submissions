import collections
N = int(input())
a = [int(input()) for i in range(N)]

table = collections.defaultdict(int)

for x in a:
    table[x] += 1

table2 = list(table.keys())
table2.sort()
for i in range(len(table2)):
    table[table2[i]] = i

b = [0]*N
for i in range(N):
    b[i] = table[a[i]]
    print(b[i])
