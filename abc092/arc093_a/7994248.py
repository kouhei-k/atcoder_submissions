N=int(input())
A=list(map(int,input().split()))

cost=[abs(A[i]-A[i+1]) for i in range(N-1)]
costsum=total=sum(cost)+abs(A[0])+abs(A[N-1])
for i in range(N):
  total=costsum
  if i == 0:
    total-=abs(A[i])
    total-=cost[i]
    total+=abs(A[i+1])
  elif i == N-1:
    total-=abs(A[i])
    total+=abs(A[i-1])
    total-=cost[i-1]
  else:
    total-=cost[i]
    total-=cost[i-1]
    total+=abs(A[i+1]-A[i-1])
  print(total)
