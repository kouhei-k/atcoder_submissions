N,X=map(int,input().split())
L=list(map(int,input().split()))

D=[0]*(N+1)

D[0]=0
count=1
for i in range(1,N+1):
  D[i]=D[i-1]+L[i-1]
  if D[i]<=X:
    count+=1
  else:
    break
print(count)
