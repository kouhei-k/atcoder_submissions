import collections
N=int(input())
table=collections.defaultdict(int)
a=list(map(int,input().split()))
for i,x in enumerate(a):
  table[i+1]=x
ans=0
for x in table:
  b=table[x]
  if table[b]==x:
    ans+=1
    table[x]=0
print(ans)
