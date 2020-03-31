N,K,M,R=map(int,input().split())
S=[int(input()) for i in range(N-1)]

S.sort(reverse=True)
ss=[0]*N
for i in range(N-1):
  ss[i+1]=ss[i]+S[i]
ans=max(0,R*K-ss[K-1])
if K<N:
  if R*K - ss[K]<=0:
    ans=0
if ans>M:
  print(-1)
else:
  print(ans)
