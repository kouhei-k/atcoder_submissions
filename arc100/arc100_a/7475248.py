import math
N=int(input())
A=list(map(int,input().split()))

B=[A[i]-i for i in range(N)]
B.sort()
temp=0

if N%2==0:
  ans = B[N//2]
  ans2= B[N//2 -1]
  temp=0
  for j in range(N):
    temp+= abs(B[j] - ans)
  temp2=0
  for j in range(N):
    temp2+= abs(B[j] - ans2)
  ans= min(temp,temp2)
else:
  ans = B[N//2]
  temp=0
  for j in range(N):
    temp+= abs(B[j] - ans )
  ans=temp
print(ans)
