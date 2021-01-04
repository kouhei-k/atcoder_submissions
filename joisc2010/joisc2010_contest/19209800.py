N,M,T,X,Y=map(int,input().split())
p=[int(input()) for i in range(M)]
d=dict()
w=dict()
ans=[0]*N
for i in range(Y):
  t,n,m,r = input().split()
  t = int(t)
  n = int(n)
  m = int(m)
  if (n,m) not in w:
      w[(n,m)]=0
  if r[0]=='o':
    d[(n,m)]=t
  elif r[0]=='i':
    
    w[(n,m)]+=1
  else:
    ans[n-1]+=max(X,p[m-1]-t+d[(n,m)]-120*w[(n,m)])
print(*ans,sep='
')
  
  
