import collections
table=collections.defaultdict(int)
N=int(input())
a=list(map(int,input().split()))

for x in a:
  table[x]+=1
  table[x+1]+=1
  table[x-1]+=1
table=list(table.values())
print(max(table))
