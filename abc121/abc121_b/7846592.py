N,M,C=map(int,input().split())
B=list(map(int,input().split()))
A=[list(map(int,input().split())) for i in range(N)]
ret=0
for i in range(N):
  ans=C
  for j in range(M):
    ans+=B[j]*A[i][j]
  if ans >0:
    ret+=1
print(ret)
