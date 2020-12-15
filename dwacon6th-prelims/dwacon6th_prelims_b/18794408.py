N=int(input())
A=list(map(int,input().split()))

mod=10**9+7
P=mod
inv_t = [0]+[1]
for i in range(2,N):
  inv_t += [inv_t[P % i] * (P - int(P / i)) % P]
K=[0]*(N-1)
k=1
for i in range(1,N):
  k*=i
  k%=mod
  K[i-1]=k
  

D=[0]*N
p=0
ans=0
for i in range(N-1):
  p+=K[-1]*inv_t[i+1]
  ans+=(A[i+1]-A[i])*p
  ans%=mod
print(ans%mod)
