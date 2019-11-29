N=int(input())
A=[int(input()) for i in range(N)]
import bisect
ans=[]
for x in A:
  id = bisect.bisect_left(ans,x)
  if id == len(ans):
    ans.append(x)
  else:
    ans[id]=x
print(len(ans))
