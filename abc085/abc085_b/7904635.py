N=int(input())
d=[int(input()) for i in range(N)]
import collections
table=collections.defaultdict(int)
for i in range(N):
  table[d[i]]+=1
print(len(table.values()))
