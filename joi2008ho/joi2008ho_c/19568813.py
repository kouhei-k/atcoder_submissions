N,M=map(int,input().split())
P=[int(input()) for i in range(N)]
P.append(0)
A=[]
for i in range(N+1):
  for j in range(N+1):
    A.append(P[i]+P[j])
A.sort()
import bisect
ans=0
for x in A:
  if x>M:
    continue
  else:
    id = bisect.bisect_left(A,M-x)
    if id>0 and ans<x+A[id-1]:
      ans=x+A[id-1]

print(ans)
