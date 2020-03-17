N=int(input())
s=[int(input()) for i in range(N)]
Q=int(input())
q=[int(input()) for i in range(Q)]

import bisect

s=[x for x in s if x>0]
s.sort()
N=len(s)
if N==0:
  print(0)
  exit(0)
for x in q:
  if x == 0:
    print(s[-1]+1)
  elif x >= N:
    print(0)
  else:
    print(s[-x-1]+1)
