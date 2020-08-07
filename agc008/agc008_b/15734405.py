N,K=map(int,input().split())
a=list(map(int,input().split()))
ans=0
tmp=0
sa=[0]*(N+1)
A=[0]*(N+1)
for i in range(N):
  sa[i+1]=sa[i]+a[i]
  if a[i]>0:
    A[i+1]=A[i]+a[i]
  else:
    A[i+1]=A[i]
for i in range(N-K+1):
  tmp=sa[i+K]-sa[i]
  tmp2=A[i]+(A[-1]-A[i+K])
  #print(max(0,tmp),tmp2)
  if max(0,tmp)+tmp2>ans:
    ans=max(0,tmp)+tmp2
print(ans)
