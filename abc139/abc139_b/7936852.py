import math
A,B=map(int,input().split())
if B==1:
  print(0)
else:
  print(math.ceil((B-1)/(A-1)))
