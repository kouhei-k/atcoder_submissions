N=int(input())
D=[int(input()) for i in range(N)]
D.sort()

A=[0]*N
import bisect

B=[0]*(N+1)
for i in range(N):
  id = bisect.bisect_left(D,D[i]//2+1)
  A[i]=id
  id = bisect.bisect_left(D,D[i]*2)
  B[i+1]=B[i]+ N-id
ans=0

for i in range(1,N-1):
  id = bisect.bisect_left(D,D[i]*2)
  ans+= A[i]*(B[-1]-B[id])
print(ans%(10**9+7))
  


  
  
