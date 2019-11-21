N=int(input())
xyh=[list(map(int,input().split()))for i in range(N)]
xyh.sort(reverse=True,key=lambda x:x[2])
for cx in range(101):
  for cy in range(101):
    H=0
    flag=False
    for i,tmp in enumerate(xyh):
      x,y,h=tmp
   
      if h != 0:
        tmp= h+abs(x-cx)+abs(y-cy)
      else:
        if H-abs(x-cx)-abs(y-cy) <=0:
          if i == N-1:
            flag=True
          continue
      if H!=0:
        if H==tmp:
         
          if i==N-1:
            flag=True
          continue
        else:
          break
      else:
        H=tmp
        

    if flag:
      print(cx,cy,H)
      exit(0)
