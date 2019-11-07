s=input()
import collections
table=collections.defaultdict(int)
for x in s:
  table[x]+=1
count=0
ans=0
for x in table:
  if table[x]%2!=0:
    count+=1
  ans+=(table[x]//2)
  
ans//=max(count,1)
ans*=2
if count >0:
  ans+=1
print(ans)
  
