import collections
table=collections.defaultdict(int)
N=int(input())
for i in range(N):
  table[input()]+=1
table=list(table.values())
table=[table[i] for i in range(len(table)) if table[i]%2==1]
print(len(table))
