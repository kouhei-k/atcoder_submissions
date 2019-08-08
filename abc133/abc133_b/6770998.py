import math
N,D=map(int,input().split())
X=[0]*N
for i in range(N):
  X[i]=list(map(int,input().split()))
count=0
for i in range(N):
  for j in range(i,N):
    dis=0
    for k in range(D):
      dis += pow(X[i][k]-X[j][k],2) 
    dis = math.sqrt(dis)

    if dis==int(dis) and dis!=0:
      count+=1
print(count)
