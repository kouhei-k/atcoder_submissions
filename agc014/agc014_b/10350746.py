N,M=map(int,input().split())
import collections
table=collections.defaultdict(int)
for i in range(M):
  a,b=map(int,input().split())
  table[a]+=1
  table[b]+=1
flag=True
for x in table:
  if table[x]%2==1:
    flag = False
    break
if flag:
  print("YES")
else:
  print("NO")
