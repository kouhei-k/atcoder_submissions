N,K=map(int,input().split())
A=[int(input()) for i in range(N)]
a=N//2
ans=0
D1=dict()
for i in range(2**a):
  tmp=0
  for j in range(a):
    if (i>>j)%2==1:
      tmp+=A[j]
  if tmp in D1:
    D1[tmp]+=1
  else:
    D1[tmp]=1
    
    
for i in range(2**(N-a)):
  tmp=0
  for j in range(N-a):
    if (i>>j)%2==1:
      tmp+=A[a+j]
  if K-tmp in D1:
    ans+=D1[K-tmp]
print(ans)
