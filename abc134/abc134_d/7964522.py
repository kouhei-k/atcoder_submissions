N=int(input())
a=list(map(int,input().split()))
b=[0]*N
for i in reversed(range(N)):
  k= N // (i+1)
  tmp=0
  for j in range(1,k):
    tmp+=b[(i+1)*(j+1)-1]
  b[i]=abs((tmp%2)-a[i])
M=sum(b)
ans=[]
for i in range(N):
  if b[i]==1:
    ans.append(i+1)
print(M)
print(" ".join(map(str,ans)))
    
