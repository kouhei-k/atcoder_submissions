N, K = map(int, input().split())
x = list(map(int, input().split()))
import bisect
id = bisect.bisect_left(x,0)
ans=10**10
if id == N:
  print(abs(x[N-K]))
  exit(0)
for i in range(max(0,(K+id)-N),min(id+1,K)):
  right = x[K+id-1-i]
  left=0
  if i>0:
    left =x[id-i]
  tmp=min(abs(left)*2+right,right*2+abs(left)) 
  ans=min(tmp,ans)
print(ans)
