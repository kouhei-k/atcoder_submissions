N=int(input())
A=list(map(int,input().split()))
ans=0
A.sort()
if N%2==0:
  for i in range(1,N,2):
    ans+=A[i]
else:
  for i in range(0,N,2):
    ans+=A[i]
print(ans)
