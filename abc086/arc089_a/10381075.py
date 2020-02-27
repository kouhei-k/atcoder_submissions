N=int(input())
pos=[0,0]
now=0
flag=True
for i in range(N):
  t,x,y=map(int,input().split())
  d = abs(x-pos[0])+abs(y-pos[1])
  if d>t-now:
    flag=False
    break
  else:
    if d%2==(t-now)%2:
      now=t
      pos[0],pos[1]=x,y
    else:
      flag=False
      break
if flag:
  print("Yes")
else:
  print("No")
