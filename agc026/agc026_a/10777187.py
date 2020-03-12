N=int(input())
a=list(map(int,input().split()))
id=1
ans=0
while(id<N):
  if a[id]==a[id-1]:
    ans+=1
    id+=2
  else:
    id+=1
print(ans)
    
