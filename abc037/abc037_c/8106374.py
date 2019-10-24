N,K=map(int,input().split())
a=list(map(int,input().split()))

tmp=sum(a[:K])
ans=sum(a[:K])
for i in range(K,N):
  tmp+= a[i]-a[i-K]
  ans+=tmp
print(ans)
  
  
