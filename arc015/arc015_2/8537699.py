N=int(input())
ans=[0]*6
def judge(Mt,mT):
  ret=[False]*6
  if Mt>=35.0:
    ret[0]=True
  elif Mt>=30:
    ret[1]=True
  elif Mt>=25:
    ret[2]=True
  if mT>=25.0:
    ret[3]=True
  if ｍT<0:
    if Mt<0:
      ret[5]=True
    else:
      ret[4]=True
  return(ret)

for i in range(N):
  M,m=map(float,input().split())
  ret=judge(M,m)
  for i in range(6):
    if ret[i]:
      ans[i]+=1
print(" ".join(map(str,ans)))
