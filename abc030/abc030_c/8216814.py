import bisect
N,M=map(int,input().split())
X,Y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
now=0
time=0
ans=0
for i in range(N+M):
  if now==0:
    id = bisect.bisect_left(a,time)
    if id >= N:
      break
    time=a[id]+X
    now=1
  else:
    id = bisect.bisect_left(b,time)
    if id >= M:
      break
    time=b[id]+Y
    now=0
    ans+=1
print(ans)
