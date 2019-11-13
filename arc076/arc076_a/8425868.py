n,m=map(int,input().split())
import math
if abs(n-m)>1:
  print(0)
  exit(0)
mod=10**9+7
ans=1
k=math.factorial(n)%mod
l=math.factorial(m)%mod
if n==m:
  ans=2
print(ans*(k*l)%mod)
