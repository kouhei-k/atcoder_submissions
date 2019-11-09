N,K=map(int,input().split())
ans=0
for i in range(K+1,N+1):
  ans += (i-K) * (N//i) + (max(0,N%i - max(K-1,0)))
print(ans)
