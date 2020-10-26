n=int(input())
s=tuple(map(int,input().split()))
xy=[[0,0] for i in range(n-1)]
for i in range(n-1):
  x,y=map(int,input().split())
  x-=s[0]
  y-=s[1]
  xy[i][0]=x
  xy[i][1]=y
m=int(input())
ab=set([tuple(map(int,input().split())) for i in range(m)])

for a,b in ab:
  d1,d2 = s[0]-a,s[1]-b
  flag=True
  for x,y in xy:
    if (a+x,b+y) in ab:
      continue
    else:
      flag=False
      break
  if flag:
    print(-d1,-d2)
    exit(0)
