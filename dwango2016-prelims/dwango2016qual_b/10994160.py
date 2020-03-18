N=int(input())
K=list(map(int,input().split()))

A=[1]*N
A[0]=K[0]
for i in range(1,N):
  A[i]=K[i-1]
for i in range(1,N-1):
  if A[i-1]==A[i] and A[i]>A[i+1]:
    A[i]=A[i+1]
print(*A)
