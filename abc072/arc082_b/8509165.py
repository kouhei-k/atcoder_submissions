N=int(input())
p=list(map(int,input().split()))
count=0
t=set()
for i in range(N):
  if p[i]==i+1:
    t.add(i)
ans=0
id=0
while(id<N):
  if id in t:
    if id+1 in t:
      id+=1
    ans+=1
  id+=1
  
  
print(ans)
