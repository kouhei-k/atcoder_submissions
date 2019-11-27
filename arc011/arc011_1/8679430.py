
m,n,N=map(int,input().split())
rm=0
ans=N
while(N+rm>=m):
  N,rm=n*((N+rm)//m),(N+rm)%m
  ans+=N
print(ans)
