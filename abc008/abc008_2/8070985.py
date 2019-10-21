import collections
N=int(input())
table=collections.defaultdict(int)
for i in range(N):
  table[input()]+=1
vote=0
ans=""
for x in table:
  if vote < table[x]:
    ans=x
    vote=table[x]
print(ans)
    
