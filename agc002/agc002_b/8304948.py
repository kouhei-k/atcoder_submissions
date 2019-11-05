import collections
N, M = map(int, input().split())
xy = [list(map(int, input().split())) for i in range(M)]
table = collections.defaultdict(int)
table2 = collections.defaultdict(int)
table2[1] += 1

for i in range(N):
    table[i+1] = 1
reached = [1]
for i in range(M):
    table[xy[i][1]] += 1
    table[xy[i][0]] -= 1
    if xy[i][0] in table2 and table2[xy[i][0]] > 0:
        table2[xy[i][0]] = table[xy[i][0]]
        table2[xy[i][1]] += table[xy[i][1]] + 1

table2 = list(table2.items())
table2 = [x for x in table2 if x[1] > 0]
print(len(table2))
