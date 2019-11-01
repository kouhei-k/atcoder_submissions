import math
N=int(input())
R=[int(input()) for i in range(N)]
R.sort(reverse=True)
s=R[0]**2
for i in range(1,N):
  if i %2==1:
    s-=R[i]**2
  else:
    s+=R[i]**2
print(math.pi*s)
