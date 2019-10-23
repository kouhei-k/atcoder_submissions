S=input()
T=int(input())

L=S.count("L")
R=S.count("R")
U=S.count("U")
D=S.count("D")
r=S.count("?")
  
x=abs(L-R)
y=abs(U-D)
if T==1:
  print(x+y+r)
else:
  if x+y>=r:
    print(x+y-r)
  else:
    k=r-(x+y)
    if k%2==0:
      print(0)
    else:
      print(1)
  
  
