import sys
import heapq
input=sys.stdin.readline
N=int(input())
A=tuple(map(int,input().split()))
hq=list(A[:N])
heapq.heapify(hq)
s=[0]*(N+1)
s[0]=sum(hq)
for i in range(N):
  x=heapq.heappop(hq)
  if x >= A[N+i]:
    s[i+1]=s[i]
    heapq.heappush(hq,x)
  else:
    s[i+1]=s[i]+A[N+i]-x
    heapq.heappush(hq,A[N+i])
    
hq=list(map(lambda x:-x, A[2*N:]))
heapq.heapify(hq)
t=[0]*(N+1)
t[-1]=-sum(hq)
for i in range(N-1,-1,-1):
  x=heapq.heappop(hq)
  x=-x
  if x <= A[N+i]:
    t[i]=t[i+1]
    heapq.heappush(hq,-x)
  else:
    t[i]=t[i+1]-x+A[N+i]
    heapq.heappush(hq,-A[N+i])
ans=-10**15
for x,y in zip(s,t):
  ans=max(x-y,ans)
print(ans)
