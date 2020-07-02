N=int(input())
XYC=[tuple(map(int,input().split())) for i in range(N)]

lx=-10**5-1
rx=10**5
ly = -10**5-1
ry=10**5
#3分探索っぽい
while(lx+0.00000001 <rx):
  prev=0
  x=(lx+rx)/2
  for X,Y,C in XYC:
    prev=max(prev,C*abs(X-x))
  
  ll=(x+lx)/2
  cost=0
  for X,Y,C in XYC:
    cost = max(cost, C*abs(X-ll))
  if cost<prev:
    rx=x
    continue
    
  rr = (x+rx)/2
  cost=0
  for X,Y,C in XYC:
    cost = max(cost, C*abs(X-rr))
  if cost < prev:
    lx=x
  else:
    lx=ll
    rx=rr

while(ly+0.00000001 <ry):
  prev=0
  y=(ly+ry)/2
  for X,Y,C in XYC:
    prev=max(prev,C*abs(Y-y))
  
  ll=(y+ly)/2
  cost=0
  for X,Y,C in XYC:
    cost = max(cost,C*abs(Y-ll))
  if cost<prev:
    ry=y
    continue
    
  rr = (y+ry)/2
  cost=0
  for X,Y,C in XYC:
    cost =  max(cost,C*abs(Y-rr))
  if cost < prev:
    ly=y
  else:
    ly=ll
    ry=rr

ans=0 
for X,Y,C in XYC:
  ans=max(ans,C*max(abs(X-lx),abs(Y-ly)))
print(ans)
