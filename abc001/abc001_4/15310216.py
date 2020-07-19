N=int(input())
SE=[tuple(map(int,input().split("-"))) for i in range(N)]
SE.sort()

ans=[]
for s,e in SE:
  s=(s//5) * 5
  if s%100==60:
    s+=40
  e=(e+4)//5 * 5
  if e%100==60:
    e+=40
  if ans and ans[-1][1]>=s:
    ans[-1][1]=max(e,ans[-1][1])
  else:
    ans.append([s,e])
for s,e in ans:
  s=str(s)
  s=s.zfill(4)
  e=str(e)
  e=e.zfill(4)
  print("-".join([s,e]))
