N,A=map(int,input().split())
B=list(map(int,input().split()))

D=[[0]*(N+1) for i in range(2501)]
D[0][0]=1
for i in range(N):
  x=B[i]
  for j in range(2500,-1,-1):
    for k in range(N-1,-1,-1):
      D[j][k+1]+=D[j-x][k]
ans=0
for i in range(1,2501):
  for j in range(1,N+1):
    if i%j==0 and j*A==i:
      ans+=D[i][j]
print(ans)
