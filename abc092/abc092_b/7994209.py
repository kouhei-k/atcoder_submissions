N=int(input())
D,X=map(int,input().split())
A=[int(input()) for i in range(N)]
ans=X
for i in range(N):
  d=1
  while(d<=D):
    ans+=1
    d+=A[i]
print(ans)
