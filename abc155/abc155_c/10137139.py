import collections
N = int(input())

S = [input() for i in range(N)]
table = collections.defaultdict(int)
for x in S:
    table[x] += 1

table = list(table.items())
table.sort(key=lambda x: x[1], reverse=True)
ans = []
k = table[0][1]
for x, i in table:
    if i == k:
        ans.append(x)
ans.sort()
for x in ans:
    print(x)
