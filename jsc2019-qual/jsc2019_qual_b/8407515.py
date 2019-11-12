N,K=map(int,input().split())
A=list(map(int,input().split()))
ans=0
mod=10**9 + 7


for i in range(N):
  count=0
  for j in range(i+1,N):
    if A[i]>A[j]:
      count+=1
  ans+=count
count=0
for i in range(N):
  for j in range(N):
    if A[i]>A[j]:
      count+=1
ans*=K
ans+=(count%mod)*(K*(K-1)//2)%mod
print(ans%mod)
