import bisect
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort()
B.sort()
C.sort()
ans=0
BC=[0]*N
for i in range(N):
  id = bisect.bisect_right(C,B[i])
  BC[i]=N-id
sBC=[0]*(N+1)
for i in range(1,N+1):
  sBC[i]=sBC[i-1]+BC[i-1]
for i in range(N):
  id=bisect.bisect_right(B,A[i])
  ans+=sBC[N]-sBC[id]
print(ans)
  
