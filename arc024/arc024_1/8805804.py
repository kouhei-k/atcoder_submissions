L,R=map(int,input().split())
l=list(map(int,input().split()))
r=list(map(int,input().split()))

id=0
import collections
ltable=collections.defaultdict(int)
rtable=collections.defaultdict(int)
for x in l:
  ltable[x]+=1
for x in r:
  rtable[x]+=1
ans=0
for x in ltable:
  ans+=min(ltable[x],rtable[x])
print(ans)
