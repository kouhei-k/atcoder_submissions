import collections
Na, Nb = map(int, input().split())
A = list(input().split())
B = list(input().split())

table = collections.defaultdict(int)
tableA = collections.defaultdict(int)
tableB = collections.defaultdict(int)
for x in A:
    table[x] += 1
    tableA[x] += 1
for x in B:
    table[x] += 1
    tableB[x] += 1
count = 0
for x in table:
    if x in tableA and x in tableB:
        count += 1
print(count / len(list(table.keys())))
