N=int(input())
s=[int(input()) for i in range(N)]
import collections
table=collections.defaultdict(int)
for x in s:
  if x%10!=0:
    table[x]+=1
if sum(s)%10==0:
  if len(table)==0:
    print(0)
  else:
    table=list(table.keys())
    table.sort()
    print(sum(s) - table[0])
else:
  print(sum(s))
