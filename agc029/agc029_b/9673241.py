N=int(input())
A=list(map(int,input().split()))
import math
import collections
powers =[2**i for i in range(1,int(math.log(max(A),2)+2))]
table=collections.defaultdict(int)
table2=collections.defaultdict(set)
ans=0
for i in range(N):
  table[A[i]]+=1
for x in table:
  for y in reversed(powers):
    if y - x in table:
      table2[x].add(y-x)
        
        
        
table2 =list(table2.items())
table2.sort(key = lambda x:len(x[1]))

for x,y in table2:
  while(table[x]>0):
    table[x]-=1
    for z in y:
      if table[z]>0:
        ans+=1
        table[z]-=1
        break
print(ans)  
      
