N,M=map(int,input().split())
ans=0
A=[]
for i in range(M):
  a,b = map(int,input().split())
  if a<N:
    ans+=N-a
    A.append(N-a)
A.sort()
if A:
  ans-=A[-1]
print(ans)
    
