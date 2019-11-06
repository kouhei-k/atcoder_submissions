import collections
N,K=map(int,input().split())
a=list(map(int,input().split()))
table=collections.defaultdict(int)
for i in range(N):
  table[a[i]]+=1
table= list(table.items())
if len(table)<=K:
  print(0)
else:
  ans=0
  table.sort(key =lambda x:x[1])
  for i in range(len(table)-K):
    ans+=table[i][1]
  print(ans)
