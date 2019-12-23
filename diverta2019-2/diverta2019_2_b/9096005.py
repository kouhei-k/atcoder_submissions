import collections
N=int(input())
xy=[tuple(map(int,input().split())) for i in range(N)]
table=collections.defaultdict(int)

for x,y in xy:
  for x2,y2 in xy:
    if x==x2 and y==y2:
      continue
    else:
      table[(x-x2,y-y2)]+=1
ans=0
for x in table:
  ans=max(ans,table[x])
print(N-ans)
