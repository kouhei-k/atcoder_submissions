n,m=map(int,input().split())
if n > 11:
  n-=12
tmp=(m/12)*6
n*=30
n+=tmp
m*=6
ans=abs(n-m)
if ans>180:
  ans=360-ans
print(ans)
