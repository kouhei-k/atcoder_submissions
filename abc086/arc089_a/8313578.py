N=int(input())
prev=[0,0,0]
for i in range(N):
  t,x,y=map(int,input().split())
  dis = abs(x-prev[0]) + abs(y -prev[1])
  time= t-prev[2]
  if dis <= time and (time-dis)%2==0:
    prev=[x,y,t]
  else:
    print("No")
    exit(0)
print("Yes")
  
