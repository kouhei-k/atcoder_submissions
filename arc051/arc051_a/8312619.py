import math
x1,y1,r=map(int,input().split())
x2,y2,x3,y3=map(int,input().split())
flag=[True,True]
if x1-r>= x2 and x1+r <=x3 and y1-r >=y2 and y1+r <=y3:
  flag[0]=False
def dis(x,y):
  return ((x-x1)**2+(y-y1)**2)**0.5
  
if dis(x2,y2) <= r and dis(x2,y3) <=r and r >= dis(x3,y2) and dis(x3,y3)<= r:
  flag[1]=False
if flag[0]:
  print("YES")
else:
  print("NO")
if flag[1]:
  print("YES")
else:
  print("NO")
