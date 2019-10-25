W,H,N=map(int,input().split())
udrl=[H,0,W,0]
for i in range(N):
  x,y,a=map(int,input().split())
  if a==1:
    udrl[3]=max(udrl[3],x)
  elif a==2:
    udrl[2]=min(udrl[2],x)
  elif a==3:
    udrl[1]=max(udrl[1],y)
  else:
    udrl[0]=min(udrl[0],y)
print((max(0,udrl[0]-udrl[1])) * (max(0,udrl[2]-udrl[3])))
    
  
