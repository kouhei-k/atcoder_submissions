import collections
N=int(input())
s=[input() for i in range(N)]
M=int(input())
t=[input() for i in range(M)]

table=collections.defaultdict(int)
for x in s:
  table[x]+=1
for x in t:
  table[x]-=1
table=table.values()
table=[x for x in table if x >= 0]
table.append(0)
print(max(table))
