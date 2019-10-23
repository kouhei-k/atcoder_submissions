import collections
N = int(input())
table = collections.defaultdict(list)

for i in range(N):
    table[int(input())].append(i)

table = list(table.keys())
table.sort()
print(table[-2])
