
N,K=map(int,input().split())
count=0
res=1
ans=0
id=0
s=[int(input()) for i in range(N)]
if 0 in s:
  print(N)
else:
  for i in range(N):
    res*=s[i]
    if res<=K:
      count+=1
      ans=max(ans,count)
    else:
      res//=s[id]
      id +=1
  print(ans)
