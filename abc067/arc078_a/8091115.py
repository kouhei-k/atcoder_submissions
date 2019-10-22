N=int(input())
a=list(map(int,input().split()))
S=[0]*(N+1)
for i in range(1,N+1):
  S[i]=S[i-1]+a[i-1]
  
ans=float("Inf")
for i in range(1,N):
  tmp=abs(S[N]-S[i]*2)
  ans=min(ans,tmp)
print(ans)
