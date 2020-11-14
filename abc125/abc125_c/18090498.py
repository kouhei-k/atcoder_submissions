N=int(input())
A=list(map(int,input().split()))


from math import gcd
B=[A[0]]*N
C=[A[-1]]*N


for i in range(1,N):
  B[i]=gcd(B[i-1],A[i])
for i in range(N-2,-1,-1):
  C[i]=gcd(C[i+1],A[i])
ans=max(B[-2],C[1])
for i in range(1,N-1):
  ans=max(gcd(B[i-1],C[i+1]),ans)
print(ans)
