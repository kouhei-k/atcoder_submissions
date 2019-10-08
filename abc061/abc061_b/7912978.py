import collections
N,M=map(int,input().split())
table=collections.defaultdict(int)
for i in range(M):
  a,b=map(int,input().split())
  table[a]+=1
  table[b]+=1
for i in range(1,N+1):
  print(table[i])
