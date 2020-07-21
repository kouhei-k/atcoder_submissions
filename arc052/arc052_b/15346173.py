import sys
input=sys.stdin.buffer.readline
from math import pi 
N,Q=map(int,input().split())
XRH=[tuple(map(int,input().split())) for i in range(N)]
#XRH.sort(key=lambda x:x[0])
V=[R*R*H for X,R,H in XRH]
for j in range(Q):
  a,b=map(int,input().split())
  ret=0
  for i in range(N):
    
    X=XRH[i][0]
    H=XRH[i][2]
    #print(X,H,a,b)
    if a<=X:
      if X+H<=b:
        ret+=V[i]
      elif b<=X:
        continue
      else:
        ret+=V[i]*(1-((X+H-b)/H)**3)
    else:
      if X+H<=a:
        continue
      elif X+H<=b:
        ret+=V[i]*((X+H-a)/H)**3
      else:
        ret-=V[i]*((X+H-b)/H)**3
        ret+=V[i]*((X+H-a)/H)**3
  print(ret*pi/3)
