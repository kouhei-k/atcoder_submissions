N,M=map(int,input().split())
import collections
table=collections.defaultdict(int)
table2=collections.defaultdict(int)
for i in range(M):
  a,b=map(int,input().split())
  if a==1:
    table[b]+=1
  if b==N:
    table2[a]+=1
for x in table:
  if x in table2:
    print("POSSIBLE")
    exit(0)
print("IMPOSSIBLE")
    
